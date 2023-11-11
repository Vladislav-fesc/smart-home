import random
from math import log
from Class.Datchik.Sensor import Sensor
class TemperatureSensor(Sensor):

  def __init__(self, sensor_id, name, floor_number):
    super().__init__(sensor_id, name, 'temperature', floor_number)

  def measure(self):
    beta = 3950  # should match the Beta Coefficient of the thermistor
    value = random.randint(0, 1024)
    celsius = 1 / (log(1 / (1023. / value - 1)) / beta + 1.0 / 298.15) - 273.15
    return celsius