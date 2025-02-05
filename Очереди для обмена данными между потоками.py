import random
import threading
import time
import queue


class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3,11))

class Cafe:
    def __init__(self,*args):
        self.queue = queue.Queue()
        self.tables = args
        self.empty_tables = len(tables)
    def guest_arrival(self,*guests):
        for i in guests:
            count=False
            for j in self.tables:
                if j.guest is None and count==False:
                    j.guest = i
                    print(f'Гость {j.guest.name} сел за стол {j.number}')
                    self.empty_tables-=1
                    count=True
                    j.guest.start()
            if count==False:
                self.queue.put(i)
                print(f'{i.name} находится в очереди')

    def discuss_guests(self):
        while self.empty_tables!=len(tables) or not self.queue.empty():
            for i in self.tables:
                if i.guest is not None and not i.guest.is_alive():
                    print(f'Гость {i.guest.name} поел и ушел, стол {i.number} свободен')
                    i.guest = None
                    self.empty_tables+=1
                if self.queue.empty() == False and i.guest==None:
                    i.guest = self.queue.get()
                    print(f'Гость {i.guest.name} вышел из очереди и сел за стол номер {i.number}')
                    self.empty_tables-=1
                    i.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()









