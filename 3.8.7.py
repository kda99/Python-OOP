'''                   Условие
Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики". Для этого требуется объявить класс TicTacToe (крестики-нолики), объекты которого создаются командой:

game = TicTacToe()
Каждый объект game должен иметь публичный атрибут:

pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.

Каждая клетка игрового поля представляется объектом класса Cell и создается командой:

cell = Cell()
Объекты класса Cell должны иметь следующие публичные локальные атрибуты:

is_free - True, если клетка свободна; False в противном случае;
value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

Также с каждым объектом класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка свободна (cell.is_free=True) и False в противном случае.

Класс TicTacToe должен иметь следующий метод:

clear() - очистка игрового поля (все клетки заполняются нулями и переводятся в закрытое состояние);

А объекты этого класса должны иметь следующую функциональность (обращение по индексам):

game[0, 0] = 1 # установка нового значения, если поле закрыто
res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)
Если указываются некорректные индексы, то должно генерироваться исключение командой:

raise IndexError('неверный индекс клетки')
Если идет попытка присвоить новое значение в открытую клетку поля, то генерировать исключение:

raise ValueError('клетка уже занята')
Также должны быть реализованы следующие полные срезы при обращении к клеткам игрового поля:

slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом indx
slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом indx
Пример использования классов (эти строчки в программе не писать):

game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
'''


class TicTacToe:  # Игровое поле
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):  # Очистка игрового поля
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def verify_index(self, value):  # Проверка корректности индекса
        if not isinstance(value, tuple) or len(value) != 2:
            raise IndexError('неверный индекс клетки')
        if any(not (0 <= x <= 3) for x in value if type(x) != slice):
            raise IndexError('неверный индекс клетки')


    def __getitem__(self, item):
        self.verify_index(item)
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c] for x in range(3))
        elif type(r) == slice:
            return tuple(self.pole[r][x] for x in range(3))

    def __setitem__(self, key, value):
        self.verify_index(key)
        r, c = key
        if self.pole[r][c]:
            self.pole[r][c].value = value.value
            self.pole[r][c].is_free = False
        else:
            raise ValueError('клетка уже занята')

class Cell:  # Клетка игрового поля
    def __init__(self):
        self.is_free = True  # True, если клетка свободна; False в противном случае
        self.value = 0  # Значение поля: 1 - крестик; 2 - нолик (по умолчанию 0)

    def __bool__(self):  # Возвращает True если клетка свободна, False если нет
        return self.is_free
