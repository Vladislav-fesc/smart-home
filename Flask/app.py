from flask import Flask, render_template
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64
import random

app = Flask(__name__)

# Имитация показателей датчика температуры
def generate_temperature():
    return round(random.uniform(0, 50), 2)

# Инициализация данных для графика
timestamps = []
temperatures = []

@app.route('/')
def index():
    temperature = generate_temperature()

    # Добавляем новые данные для графика
    timestamps.append(datetime.now().strftime('%H:%M:%S'))
    temperatures.append(temperature)

    # Ограничиваем количество точек на графике
    if len(timestamps) > 10:
        timestamps.pop(0)
        temperatures.pop(0)

    return render_template(
        'index.html',
        temperature=temperature
    )

@app.route('/plot.png')
def plot():
    # Создаем график с показателями температуры
    fig, ax = plt.subplots()
    ax.plot(timestamps, temperatures, marker='o', linestyle='-', color='b')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temperature Trends')
    
    # Сохраняем график в байтовый объект
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    # Кодируем байтовый объект в base64
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return f'<img src="data:image/png;base64,{plot_url}" alt="Temperature Trends">'

if __name__ == '__main__':
    app.run(debug=True)

