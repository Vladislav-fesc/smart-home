import random
class signall:
    def __init__(self,singl):
        self.lightscom1 = True
        self.lightscom2= True
        self.lightscom3 = True
        self.lightskit = True
        self.lightszal = True
        self.lightsbath = True
        self.lightskorid= True
        self.lightstoilet= True
        self.air_conditioner1 = True
        self.air_conditioner2 = True
        self.air_conditioner3 = True
        self.air_conditioner4 = True
        self.signal= singl

    def off(self):
        if self.signal == True:
            print('Выключаем все кроме датчиков дыма буровня воды и сигнализациии')
            self.lightscom1 = False
            self.lightscom2= False
            self.lightscom3 = False
            self.lightskit = False
            self.lightszal = False
            self.lightsbath = False
            self.lightskorid= False
            self.lightstoilet= False
            self.air_conditioner1 = False
            self.air_conditioner2 = False
            self.air_conditioner3 = False
            self.air_conditioner4 =False
        else:
            print('дом работает')
class tempertur:
    def __init__(self,con1,con2,con3,con4):
        self.air_conditioner1 = True
        self.air_conditioner2 = True
        self.air_conditioner3 = True
        self.air_conditioner4 = True
        self.temp1=con1
        self.temp2=con2
        self.temp3=con3
        self.temp4=con4
    def temperatur(self):
        if self.temp1 >= 26:
            print ("включить кондиционер на поижение температуры ")
        elif self.temp1<=14:
             print ("включить кондиционер на повышение температуры температуры ")
        else:
            print("выключить кондиционер")
            self.air_conditioner1 = False
        if self.temp2>= 26:
            print ("включить кондиционер на поижение температуры ")
        elif self.temp2<=14:
             print ("включить кондиционер на повышение температуры температуры ")
        else:
            print("выключить кондиционер")
            self.air_conditioner1 = False
        if self.temp3 >= 26:
            print ("включить кондиционер на поижение температуры ")
        elif self.temp3<=14:
             print ("включить кондиционер на повышение температуры температуры ")
        else:
            print("выключить кондиционер")
            self.air_conditioner1 = False
        if self.temp4 >= 26:
            print ("включить кондиционер на поижение температуры ")
        elif self.temp4<=14:
             print ("включить кондиционер на повышение температуры температуры ")
        else:
            print("выключить кондиционер")
            self.air_conditioner1 = False
class WindowSensor:
    def __init__(self,com):
        self.window_open = com  # Изначально окно закрыто
        self.air_conditioner = False  # Кондиционер изначально выключен

    def window(self):
        if self.window_open == True:
            print("окно открыто")
            self.turn_off_air_conditioner()
        else:
            print("окно закрыто")
            self.turn_on_air_conditioner()

    def turn_on_air_conditioner(self):
        self.air_conditioner = True
        print("кондиционер работает")

    def turn_off_air_conditioner(self):
        self.air_conditioner = False
        print("выключить кондиционер")

    def monitor_window(self):
        if self.window_open:
            self.window()  # Если окно открыто, выключаем кондиционер
        else:
             self.window() # Если окно закрыто, включаем кондиционер
test_list = [True,False]
window_sensor = WindowSensor(test_list[random.randint(0,1)])
window_sensor.monitor_window() 
my_home = signall(test_list[random.randint(0,1)])
my_home.off()
temper = tempertur(13,14,15,16)
temper.temperatur()

