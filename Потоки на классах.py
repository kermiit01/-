import threading
import time
class Knight(threading.Thread):
    def __init__(self,name,power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, На нас напали!')
        enemy=100
        count=0
        while enemy>0:
            enemy-=self.power
            count+=1
            time.sleep(1)
            print(f' {self.name} сражается {count} дней, врагов осталось {enemy}')
        print(f" {self.name} одержал победу! Он сделал это за {count} дней.")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
first_knight.join()
print(f'Все битвы закончились!')
