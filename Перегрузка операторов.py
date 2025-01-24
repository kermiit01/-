class House:
    def __init__(self,name,floor):
        self.name = name
        self.floor = floor
    def go_to(self):
        print(f'Вы в доме под названием "{self.name}", в нем {self.floor} этажей')
        i=int(input('Введите этаж на который хотите переехать - '))
        a=0
        if self.floor < i:
            print('Такого этажа не существует')
        else:
            while a != i:
                a += 1
                print(a)
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


h1=House('Крутой дом', 5)
h2 = House('Домик в деревне', 20)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

