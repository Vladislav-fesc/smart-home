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
