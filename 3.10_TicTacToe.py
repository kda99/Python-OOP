import random


class Cell:
    def __init__(self):
        self.value = 0  # текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик

    def __setattr__(self, key, value):
        if key == 'value' and value in range(3):
            object.__setattr__(self, key, value)

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3))  for _ in range(3))

    def verify_index(self, item):
        if item[0] not in [0,1,2] or item[1] not in [0,1,2]:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.verify_index(item)
        return self.pole[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.verify_index(key)
        self.pole[key[0]][key[1]].value = value

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def show(self):
        pass

    def human_go(self):
        return list(map(int,input('Введите координаты выбранной клетки через пробел: ').split()))

    def computer_go(self):
        while True:
            if
