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
    STEP_COUNTER = 0
    d = {FREE_CELL: ' ', HUMAN_X: 'X', COMPUTER_O: 'O'}

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, item):
        self.__is_human_win = item

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, item):
        self.__is_computer_win = item

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, item):
        self.__is_draw = item

    def verify_index(self, value):  # Проверка корректности индекса
        if not isinstance(value, tuple) or len(value) != 2:
            raise IndexError('некорректно указанные индексы')
        if any(not (0 <= x <= 2) for x in value if type(x) != slice):
            raise IndexError('некорректно указанные индексы')

    def verify_diag(self, item):
        if all(self.pole[i][j].value == item for i in range(3) for j in range(3) if i == j):
            return True
        if all(self.pole[i][j].value == item for i in range(3) for j in range(3) if i + j == 2):
            return True
        else:
            return False

    def verify_row(self, item):
        return any(all(map(lambda x: x.value == item, row)) for _ in range(3) for row in self.pole)

    def verify_col(self, item):
        zipped_rows = zip(*self.pole)
        return any(all(map(lambda x: x.value == item, row)) for _ in range(3) for row in zipped_rows)

    def verify_win(self, item: int):
        self.STEP_COUNTER += 1
        flag = any((self.verify_col(item), self.verify_row(item), self.verify_diag(item)))
        if flag:
            if item == self.HUMAN_X:
                self.is_human_win = True
            else:
                self.is_computer_win = True
        elif self.STEP_COUNTER > 8:
            self.is_draw = True

    def __getitem__(self, item):
        self.verify_index(item)
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(3))
        elif type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(3))
        else:
            return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.verify_index(key)
        r, c = key
        if self.pole[r][c]:
            self.pole[r][c].value = value
            self.pole[r][c].is_free = False
        else:
            raise ValueError('клетка уже занята')

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def show(self):
        print(' --- --- ---')
        print('| ' + self.d[self.pole[0][0].value] + ' | ' + self.d[self.pole[0][1].value] + ' | ' + self.d[
            self.pole[0][2].value] + ' |')
        print(' --- --- ---')
        print('| ' + self.d[self.pole[1][0].value] + ' | ' + self.d[self.pole[1][1].value] + ' | ' + self.d[
            self.pole[1][2].value] + ' |')
        print(' --- --- ---')
        print('| ' + self.d[self.pole[2][0].value] + ' | ' + self.d[self.pole[2][1].value] + ' | ' + self.d[
            self.pole[2][2].value] + ' |')
        print(' --- --- ---')


    def human_go(self):
        while True:
            tmp = list(map(int, input('Введите координаты выбранной клетки через пробел: ').split()))
            if self.pole[tmp[0]][tmp[1]].value == 0:
                self.pole[tmp[0]][tmp[1]].value = self.HUMAN_X
                self.verify_win(self.HUMAN_X)
                break

    def computer_go(self):
        while True:
            tmp = [random.randint(0, 2), random.randint(0, 2)]
            if not self.pole[tmp[0]][tmp[1]].value:
                self.pole[tmp[0]][tmp[1]].value = self.COMPUTER_O
                self.verify_win(self.COMPUTER_O)
                break

    def __bool__(self):
        return not any((self.is_draw, self.is_human_win, self.is_computer_win))



cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"






# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")
