from flask import Flask, render_template, jsonify
from datetime import datetime
import random
import plotly
import plotly.graph_objs as go

app = Flask(__name__)

# Имитация данных с датчиков
sensor_data = {
    'temperature1': 25.0,
    'temperature2': 22.5,
    'temperature3': 24.0,
    'temperature4': 23.5
}

light_status = False
temperature_history = []
time_history = []

@app.route('/')
def index():
    return render_template('index.html', sensor_data=sensor_data, light_status=light_status)

@app.route('/update_data', methods=['POST'])
def update_data():
    global temperature_history, time_history, light_status

    # Обновление данных с датчиков
    for sensor in sensor_data:
        sensor_data[sensor] = round(sensor_data[sensor] + (0.5 - 1.0 * random.random()), 2)

    # Добавление новых данных в историю
    current_time = datetime.now().strftime('%H:%M:%S')
    time_history.append(current_time)
    temperature_history.append(sensor_data['temperature1'])

    # Ограничение истории в 20 точках
    if len(temperature_history) > 20:
        temperature_history = temperature_history[-20:]
        time_history = time_history[-20:]

    # Обновление статуса света (для примера, используем случайное значение)
    light_status = not light_status

    # Возвращение данных в формате JSON для обновления веб-страницы
    return jsonify({'sensor_data': sensor_data, 'light_status': light_status, 'time_history': time_history, 'temperature_history': temperature_history})

if __name__ == '__main__':
    app.run(debug=True)

