import threading
import time
# Создание класса
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        n = int(100/self.power)
        for i in range(1, n+1):
            print(f'{self.name} сражается {i} дней, осталось {100-i*self.power} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {n} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
thread1 = first_knight
thread2 = second_knight
thread1.start()
thread2.start()
thread1.join()
thread2.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
