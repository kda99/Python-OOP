"""                                             Условие
Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)
где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число); salary - зарплата (число: целое или вещественное); year_job - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old, salary, year_job и соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:

data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)
При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
Пример использования класса (эти строчки в программе не писать):

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""

class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.lst = [fio, job, old, salary, year_job]
        self.tmp = self.lst[::]
        self.fio = self.lst[0]
        self.job = self.lst[1]
        self.old = self.lst[2]
        self.salary = self.lst[3]
        self.year_job = self.lst[4]

    def __setattr__(self, key, value):  # Проверка соответствия типа данных атрибуту класса
        if key in ('fio', 'job') and isinstance(value, str):
            object.__setattr__(self, key, value)
        elif key in ('old', 'year_job') and isinstance(value, int):
            object.__setattr__(self, key, value)
        elif key == 'salary' and isinstance(value, (int, float)):
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)
    def verify_index(self, item):
        if item not in range(5):
            raise IndexError('неверный индекс')

    def __next__(self):
        if len(self.tmp) > 0:
            return self.tmp.pop(0)
        else:
            self.tmp = self.lst[::]
            raise StopIteration

    def __iter__(self):
        return self

    def __getitem__(self, item):
        self.verify_index(item)
        return self.lst[item]

    def __setitem__(self, key, value):
        self.verify_index(key)
        self.lst[key] = value
        self.tmp = self.lst[::]


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
t = iter(pers)
[print(next(t)) for _ in range(5)]