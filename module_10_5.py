import multiprocessing
from _datetime import datetime

def read_info(name):
    all_data = []
    file = open(name, 'r')
    for i in file.readline():
        if i != "":
            all_data.append(i)
    file.close()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

start = datetime.now()
for i in filenames:
    read_info(i)
fin = datetime.now()
print(f'{fin-start} (линейный)')

# Многопроцессный

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as Pool:
        start1 = datetime.now()
        Pool.map(read_info, filenames)
        fin1 = datetime.now()
        print(f'{fin1-start1} (многопроцессный)')
