"""                                                  Условие
 В программе необходимо реализовать таблицу TableValues по следующей схеме:



Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

cell = Cell(data)
где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с атрибутом type_data объекта класса TableValues), должно генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')
При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, item):
        self.__data = item


class TableValues:
    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.index_iter = -1

    def verify_type(self, item):
        if type(item) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')

    def verify_index(self, item):
        if len(item) == 2 and isinstance(item[0], int) and isinstance(item[1], int):
            if item[0] < self.rows and item[1] < self.cols:
                return
            else:
                raise IndexError('неверный индекс')

    def __setattr__(self, key, value):
        if key in ('rows', 'cols') and isinstance(value, int):
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def __setitem__(self, key, value):
        self.verify_type(value)
        self.verify_index(key)
        row, col = key
        self.table[row][col] = value

    def __getitem__(self, item):
        self.verify_index(item)
        row, col = item
        return self.table[row][col]

    def __iter__(self):
        self.table = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.index_iter = 0
        return self

    def __next__(self):
        if len(self.table) - 1 > self.index_iter:
            self.index_iter += 1
            return self.table[self.index_iter]
        else:
            raise StopIteration("Значения в таблице закончились")


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов " \
                                                  "for, должен сначала возвращаться итератор для строк, а затем, этот " \
                                                  "итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
