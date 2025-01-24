class House:
    def __init__(self,name,floor):
        self.name = name
        self.floor = floor
        self.go_to()
    def go_to(self):
        print(f'Вы в доме под названием "{self.name}", во нем {self.floor} этажей')
        i=int(input('Введите этаж на который хотите переехать - '))
        a=0
        if self.floor < i:
            print('Такого этажа не существует')
        else:
            while a != i:
                a += 1
                print(a)


h1=House('Крутой дом', 5)
h2 = House('Домик в деревне', 20)