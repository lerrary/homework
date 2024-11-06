# Импорты необходимых модулей и функций
import time
import threading
from _datetime import datetime

# Объявление функции write_words
def write_words(word_count, file_name):
    time.sleep(0.1)
    file = open(file_name, 'a', encoding="utf=8")
    for i in range(word_count):
        file.write(f'Какое-то слово № {i}\n')
    file.close()
    print(f'Завершилась запись в файл {file_name}')

# Взятие текущего времени
start = datetime.now()
# Запуск функций с аргументами из задачи
write_words (10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
fin = datetime.now()
# Вывод разницы начала и конца работы функций
print(f'работа потоков {fin-start}')
# Взятие текущего времени
start1 = datetime.now()
# Создание и запуск потоков с аргументами из задачи
thread1 = threading.Thread(write_words(10, 'example5.txt'))
thread1.start()
thread1.join()
thread2 = threading.Thread(write_words(30, 'example6.txt'))
thread2.start()
thread2.join()
thread3 = threading.Thread(write_words(200, 'example7.txt'))
thread3.start()
thread3.join()
thread4 = threading.Thread(write_words(100, 'example8.txt'))
thread4.start()
thread4.join()

# Взятие текущего времени
fin1 = datetime.now()
# Вывод разницы начала и конца работы потоков
print(f'работа потоков {fin1-start1}')
