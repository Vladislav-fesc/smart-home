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
        self.lights = True
        self.air_conditioner = True
        self.signal= singl

    def off(self,):
        if self.signal == True:
            print('Выключаем все кроме датчиков дыма буровня воды и сигнализациии')
        else:
            print('дом работает')
test_list = [True,False]
my_home = signall(test_list[random.randint(0,1)])
my_home.off()

