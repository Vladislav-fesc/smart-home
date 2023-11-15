from flask import Flask, render_template, request, redirect
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime
import pandas as pd

app = Flask(__name__)

# Mockup данных с датчиков
sensor_data = {
    'temperature': [],
    'humidity': [],
}

light_status = False  # Статус света: выключен

# Функция для создания графика
def generate_plot():
    # Добавим текущее время и минуты в данные
    current_time = datetime.now()
    sensor_data['time'] = current_time
    sensor_data['minutes'] = current_time.minute

    # Добавим данные в списки
    sensor_data['temperature'].append(current_time.second % 30 + 20)
    sensor_data['humidity'].append(current_time.second % 40 + 30)

    # Ограничим количество точек на графике
    max_points = 10
    if len(sensor_data['temperature']) > max_points:
        for key in sensor_data:
            sensor_data[key] = sensor_data[key][-max_points:]

    # Создаем DataFrame с данными
    df = pd.DataFrame(sensor_data)

    # Создаем график на основе данных с датчиков и времени
    fig, ax = plt.subplots()
    df.plot(x='minutes', y=['temperature', 'humidity'], ax=ax)
    ax.set_xlabel('Minutes')
    ax.set_ylabel('Value')
    ax.set_title('Sensor Data')

    # Сохраняем график в памяти
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)  # Закрываем график, чтобы избежать проблемы с потоками

    # Кодируем изображение в base64 для встраивания в HTML
    return base64.b64encode(img.getvalue()).decode('utf-8')

# Главная страница
@app.route('/')
def index():
    plot_data = generate_plot()
    return render_template('index.html', sensor_data=sensor_data, light_status=light_status, plot_data=plot_data)

# Обработчик кнопки для управления светом
@app.route('/toggle_light', methods=['POST'])
def toggle_light():
    global light_status
    light_status = not light_status
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
