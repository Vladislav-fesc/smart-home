from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import random

app = Flask(__name__)

# Генерация случайных данных для температуры и времени
def generate_data():
    data = {'temperature': [], 'time': []}
    current_temperature = 25.0  # начальная температура
    for i in range(10):  # 10 точек данных для примера
        current_temperature += random.uniform(-1, 1)  # случайное изменение температуры
        data['temperature'].append(round(current_temperature, 2))
        data['time'].append(i + 1)  # минуты
    return data

# Создание графика
def create_plot(data):
    plt.plot(data['time'], data['temperature'], marker='o')
    plt.title('Показатели температуры')
    plt.xlabel('Время (минуты)')
    plt.ylabel('Температура (°C)')
    plt.grid(True)
    # Сохранение графика в байтовом представлении
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()
    return base64.b64encode(image_stream.getvalue()).decode('utf-8')

@app.route('/')
def index():
    data = generate_data()
    plot_image = create_plot(data)
    return render_template('index.html', temperature_data=data, plot_image=plot_image)

if __name__ == '__main__':
    app.run(debug=True)
