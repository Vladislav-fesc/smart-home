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
    # Combine time and temperature into a list of tuples
    data['time_and_temperature'] = list(zip(data['time'], data['temperature']))
    return data

# Создание графика
def create_plot(fig, data):
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(data['time'], data['temperature'], marker='o')
    ax.set_title('Показатели температуры')
    ax.set_xlabel('Время (минуты)')
    ax.set_ylabel('Температура (°C)')
    ax.grid(True)

@app.route('/')
def index():
    data = generate_data()
    fig, ax = plt.subplots()
    create_plot(fig, data)
    # Save fig in bytes
    image_stream = BytesIO()
    fig.savefig(image_stream, format = 'png')
    plt.close(fig)
    plot_image = base64.b64encode(image_stream.getvalue()).decode('utf-8')
    return render_template('index.html', temperature_data=data['time_and_temperature'], plot_image=plot_image)

if __name__ == '__main__':
    app.run(debug=True)
