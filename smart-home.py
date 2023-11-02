import random
from Class.Signall import signall
from Class.ClimateControl import tempertur
from Class.WindowSensor import WindowSensor
test_list = [True,False]
window_sensor = WindowSensor(test_list[random.randint(0,1)])
window_sensor.monitor_window() 
my_home = signall(test_list[random.randint(0,1)])
my_home.off()
temper = tempertur(13,14,15,16)
temper.temperatur()

