'''                                     Условие
Известно, что с объектами класса tuple можно складывать только такие же объекты (кортежи). Например:

t1 = (1, 2, 3)
t2 = t1 + (4, 5) # (1, 2, 3, 4, 5)
Если же мы попытаемся прибавить любой другой итерируемый объект, например, список:

t2 = t1 + [4, 5]
то возникнет ошибка. Предлагается поправить этот функционал и создать свой собственный класс Tuple, унаследованный от базового класса tuple и поддерживающий оператор:

t1 = Tuple(iter_obj)
t2 = t1 + iter_obj  # создается новый объект класса Tuple с новым (соединенным) набором данных
где iter_obj - любой итерируемый объект (список, словарь, строка, множество, кортеж и т.п.)
'''


class Tuple(tuple):
    @staticmethod
    def iter_obj_to_tuple(iter_obj):
        return tuple(i for i in iter_obj)

    def __init__(self, iter_obj):
        if type(iter_obj) != tuple:
            iter_obj = self.iter_obj_to_tuple(iter_obj)
        self.tpl = iter_obj

    def __add__(self, other):
        if type(other) != tuple:
            other = self.iter_obj_to_tuple(other)
        return Tuple(self.tpl + other)


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"

