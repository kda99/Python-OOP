'''                                     Условие
Объявите в программе базовый класс с именем IteratorAttrs для перебора всех локальных атрибутов объектов класса.
Напомню, что для этого используются два магических метода:

__iter__() - для получения объекта-итератора (в данном случае - это сам объект self)
__next__() - для перебора локальных атрибутов объекта self (используйте для этого словарь __dict__)

Метод __next__() на каждой итерации должен возвращать кортеж в формате: (имя атрибута, значение).

Подсказка: здесь можно определить один метод __iter__() как функцию-генератор.

Объявите дочерний класс SmartPhone, объекты которого создаются командой:

phone = SmartPhone(model, size, memory)
где model - модель смартфона (строка); size - габариты (ширина, длина) в виде кортежа двух чисел; memory - размер ОЗУ
(памяти), как целое число. В каждом объекте класса SmartPhone должны создаваться соответствующие локальные атрибуты:
model, size, memory.

Благодаря наследованию от базового класса IteratorAttrs, с объектами класса SmartPhone должен выполняться оператор for:

for attr, value in phone:
    print(attr, value)
'''

class IteratorAttrs:
    def __iter__(self):
        for elem in self.__dict__.items():
            yield elem


class SmartPhone(IteratorAttrs):
    def __init__(self, model: str, size: tuple, memory: int):
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone('nokia', (50, 120), 5)
for attr, value in phone:
    print(attr, value, sep=': ')