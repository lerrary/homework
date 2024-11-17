import pandas as pd
import numpy as np

# создание массива из нескольких строк и столбцов из случайных чисел

tuples = [
   ["raw1", "raw1", "raw2", "raw2", "raw3", "raw3", "raw4", "raw4"],
   ["one", "two", "one", "two", "one", "two", "one", "two"],
]


index = pd.MultiIndex.from_arrays(tuples, names=["1", "2"])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["column1", "column2"])

df2 = df[:8]

print (df2)

#создает таблицу с данными в формате True/False на основании заданного алгоритма (list)

df = pd.DataFrame({"key": list("abccba"), "data1": range(6)})

print (pd.get_dummies(df["key"]))

import requests

# печать адресной строки сайта
# и его кодировки

r = requests.get('https://dzen.ru/a/ZzSOL36qjXBLMjkc')
print (r.url)
print(r.encoding)
