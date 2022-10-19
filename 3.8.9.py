"""                                   Условие
Вам необходимо описывать в программе очень большие и разреженные таблицы данных (с большим числом пропусков). Для этого предлагается объявить класс SparseTable, объекты которого создаются командой:

st = SparseTable()
В каждом объекте этого класса должны создаваться локальные публичные атрибуты:

rows - общее число строк таблицы (начальное значение 0);
cols - общее число столбцов таблицы (начальное значение 0).

В самом классе SparseTable должны быть объявлены методы:

add_data(row, col, data) - добавление данных data (объект класса Cell) в таблицу по индексам row, col (целые неотрицательные числа);
remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами (row, col).

При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows, cols объекта класса SparseTable. Если происходит попытка удалить несуществующую ячейку, то должно генерироваться исключение:

raise IndexError('ячейка с указанными индексами не существует')
Ячейки таблицы представляют собой объекты класса Cell, которые создаются командой:

data = Cell(value)
где value - данные ячейки (любой тип).

Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж) i, j, а значениями - объекты класса Cell.

Также с объектами класса SparseTable должны выполняться команды:

res = st[i, j] # получение данных из таблицы по индексам (i, j)
st[i, j] = value # запись новых данных по индексам (i, j)
Чтение данных возможно только для существующих ячеек. Если ячейки с указанными индексами нет, то генерировать исключение командой:

raise ValueError('данные по указанным индексам отсутствуют')
При записи новых значений их следует менять в существующей ячейке или добавлять новую, если ячейка с индексами (i, j) отсутствует в таблице. (Не забывайте при этом пересчитывать атрибуты rows и cols).

Пример использования классов (эти строчки в программе не писать):

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table = {}

    def update_index(self):
        self.rows = max(i[0] for i in self.table) + 1
        self.cols = max(i[1] for i in self.table) + 1

    def add_data(self, row, col, data):
        self.table[(row, col)] = Cell(data)
        self.update_index()

    def remove_data(self, row, col):
        if (row, col) not in self.table:
            raise IndexError('ячейка с указанными индексами не существует')
        else:
            del self.table[((row, col))]
            self.update_index()


    def __getitem__(self, item):
        if (item[0], item[1]) not in self.table:
            raise ValueError('данные по указанным индексам отсутствуют')
        else:
            return self.table[(item[0], item[1])].value

    def __setitem__(self, key, value):
        if key in self.table:
            self.table[key] = value
        else:
            row, col = key
            self.add_data(row, col, value)
            self.update_index()


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"