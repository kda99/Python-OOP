'''                                             Условие
Создается проект, в котором предполагается использовать списки из целых чисел. Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:

__init__()
__setitem__()
append()

так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных, генерировать исключение командой:

raise TypeError('можно передавать только целочисленные значения')
'''


class ListInteger(list):
    def verify_int(self, lst):
        if not all(map(lambda x: type(x) == int, lst)):
            raise TypeError('можно передавать только целочисленные значения')

    def __init__(self, lst):
        self.verify_int(lst)
        super().__init__(lst)

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)


    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().append(value)

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError