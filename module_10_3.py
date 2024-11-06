import threading
import time
import random
lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and lock.locked():
                lock.release()
            bal_up = random.randint(50, 500)
            self.balance += bal_up
            print(f'Пополнение: {bal_up}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            bal_d = random.randint(50, 500)
            print(f'Запрос на {bal_d}')
            if bal_d <= self.balance:
                self.balance -= bal_d
                print(f'Снятие: {bal_d}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()
bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
