class House:
    houses_history=[]

    def  __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return cls.houses_history
    def __init__(self,name,floor):
        self.name = name
        self.floor = floor
    def __del__(self):
        print(f'{self.name} был снесен, его существование сохранилось в базе данных')
    def __len__(self):
        return self.floor
    def __str__(self):
        return f'Вы в доме под названием "{self.name}", в нем {self.floor} этажей'
    def __eq__(self, other):
        if isinstance(other, House):
            return self.floor == other.floor
        elif isinstance(other, int):
            return self.floor == other.floor
    def __lt__(self, other):
        return self.floor < other.floor
    def __le__(self, other):
        return self.floor <= other.floor
    def __gt__(self, other):
        return self.floor > other.floor
    def __ne__(self, other):
        return self.floor != other.floor
    def __add__(self, value):
        if isinstance(value,House):
            self.floor += value
            return self
        elif isinstance(value,int):
            self.floor += value
            return self
    def __radd__(self, value):
        self.__add__(value)
        return self
    def __iadd__(self, value):
        self.__add__(value)
        return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
