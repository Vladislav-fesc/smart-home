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