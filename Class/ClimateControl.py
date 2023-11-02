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