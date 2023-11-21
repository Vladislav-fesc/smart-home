import random
from Class.ClimateControl import tempertur
from Class.WindowSensor import WindowSensor
from Class.Datchik.temperatur import TemperatureSensor
test_list = [True,False]
window_sensor = WindowSensor(test_list[random.randint(0,1)])
window_sensor.monitor_window() 
temper = TemperatureSensor(1, 'TESET', 5)
temper1 = tempertur(temper.measure(),0,0,0)
temper1.temperatur()