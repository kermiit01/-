class Car:
    model =''
    __vin = 0
    __numbers = ''
    def __init__(self,model,vin,numbers):
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.model=model
            self.__vin=vin
            self.__numbers=numbers
        else:
            print('Данные не были созданы')


    def __is_valid_vin(self,vin):
        if vin<1000000 or vin>9999999:
            raise IncorrectVinNumber
        if isinstance(vin,int):
            return True
        else:
            raise IncorrectVinNumber

    def __is_valid_numbers(self,number):
        if isinstance(number,str):
            if len(number)==6:
                return True
            else:
                raise IncorrectCarNumbers
        else:
            raise IncorrectCarNumbers


class IncorrectVinNumber(Exception):
    message = 'Не верный vin машины'
class IncorrectCarNumbers(Exception):
    message ='Не верный номер машины'

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


