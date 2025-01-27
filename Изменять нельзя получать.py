class Vehicle:

    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''
    __color_variants= ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,owner,model,color,engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        check = False
        for i in self.__color_variants:
            if color.lower() == i.lower():
                self.__color = color
                check = True
                break
        if check == False:
            print(f'Нельзя зазнести машину с цветом {color}')
    def get_model(self):
        print(f'Модель автомобиля: {self.__model}')
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power} л.с.')
    def get_color(self):
        print(f'Цвет автомобиля: {self.__color}')
    def print_info(self):

        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец машины: {self.owner}')
    def set_color(self,color):
        check = False
        for i in self.__color_variants:
            if color.lower() == i.lower():
                self.__color = color
                check = True
                break
        if check == False:
            print(f'Нельзя изменить цвет авто на {color}')
class Sedan(Vehicle):
    _passenger_limit=5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()