import random as r
class Animal:
    live =True
    sound = None
    _degree_of_danger = 0
    _cords =[0,0,0]
    speed = 0
    def __init__(self,speed): # Так как скорость мы определяем при создании объекта, но она нигде не учавствует, её множитель я добавил к передвижению по координатам, так же можно сделать её лимитом передвижения равной максимальной гипотинузе при трехмерном передвижении
        self.speed = speed
    def move(self,dx,dy,dz):
        self._cords[0] += dx*self.speed
        self._cords[1] += dy*self.speed
        self._cords[2] += dz*self.speed
        if self._cords[2]<0:
            print("It's too deep, i can't dive :(")
            self._cords[2]-=dz
    def get_cords(self):
        print(f'X:{self._cords[0]} Y:{self._cords[1]} Z:{self._cords[2]}')
    def attack(self):
        if self._degree_of_danger <5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {r.randint(1,4)} eggs for you")

class AquaticAnimal(Animal):
    _degree_of_danger = 3
    def dive_in(self,dz):
        super()._cords[2]-=abs(dz/2*super().speed)

class PoisonousAnimal(Animal):
    _degree_of_danger = 8

class Duckbill(Bird,AquaticAnimal,PoisonousAnimal):
    sound = 'Click-click-click'



db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

