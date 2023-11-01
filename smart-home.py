import random
'''import datetime
def Signal:
    if signal == True:
    Выключаем все кроме датчика воды в ваной 
   '''
    
'''def time:
    current_time = datetime.datetime.now().time()
    if urrent_time >= datetime.time(22, 0) or current_time <= datetime.time(6, 0):
            выключаем свет во всем доме и кондецианеры 

       '''
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
    def __init__(self,con1):
        self.air_conditioner1 = True
        self.air_conditioner2 = True
        self.air_conditioner3 = True
        self.air_conditioner4 = True
        self.temp1=con1
    def temperatur(self):
        if self.temp1 >= 26:
            print ("включить кондиционер на поижение температуры ")
        elif self.temp1<=14:
             print ("включить кондиционер на повышение температуры температуры ")
        else:
            print("выключить кондиционер")
            self.air_conditioner1 = True
    def conder(self):
        self.air_conditioner4 =False
test_list = [True,False]
my_home = signall(test_list[random.randint(0,1)])
my_home.off()
temper = tempertur(13)
temper.temperatur()

