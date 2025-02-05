import random
import threading
import time
class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            time.sleep(0.01)
            add=random.randint(50, 501)
            self.balance += add
            print(f'Пополнение {add}. Текущий баланс: {self.balance}')
            if self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            time.sleep(0.01)
            take = random.randint(50,501)
            if take <= self.balance:
                self.balance-= take
                print(f'Снятие {take}. Текущий баланс: {self.balance}')
            else:
                print(f'Не достаточно средств, запрос отклонен')
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()