class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = str(model)
        self.__vin = Car.__is_valid_vin(__vin)
        self.__numbers = Car.__is_valid_numbers(__numbers)

    def __is_valid_vin(vin_number):
        if isinstance(vin_number, int) == False:
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    def __is_valid_numbers(numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectVinNumber("Некорректный тип данных для номеров")
        elif len(numbers) != 6:
            raise IncorrectVinNumber("Неверная длина номера")
        else:
            return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
