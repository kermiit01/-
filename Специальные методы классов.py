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
        return print(f'Вы в доме под названием "{self.name}", в нем {self.floor} этажей')


h1=House('Крутой дом', 5)
h2 = House('Домик в деревне', 20)
print(len(h2))
print(h1)