'''                                     Условие
 Объявите в программе следующие классы без содержимого (используйте оператор pass):

Protists, Plants, Animals, Mosses, Flowering, Worms, Mammals, Human, Monkeys

и постройте схему наследования в соответствии со следующей иерархией древа жизни:



Затем, объявите в программе классы:

Monkey - наследуется от Monkeys и служит для описания обезьян;
Person - наследуется от Human и служит для описания человека;
Flower - наследуется от Flowering и служит для описания цветка;
Worm - наследуется от Worms и служит для описания червей.

Объекты этих классов должны создаваться командами:

obj = Monkey(name, weight, old)
obj = Person(name, weight, old)
obj = Flower(name, weight, old)
obj = Worm(name, weight, old)
где name - наименование (или имя) объекта (строка); weight - вес (вещественное число); old - возраст (целое число). В каждом объекте любого из этих классов должны создаваться соответствующие атрибуты: name, weight, old.

Создайте в программе следующие объекты и сохраните их в виде списка lst_objs:

Monkey: "мартышка", 30.4, 7
Monkey: "шимпанзе", 24.6, 8
Person: "Балакирев", 88, 34
Person: "Верховный жрец", 67.5, 45
Flower: "Тюльпан", 0.2, 1
Flower: "Роза", 0.1, 2
Worm: "червь", 0.01, 1
Worm: "червь 2", 0.02, 1

Затем, используя функции isinstance() и генератор списков (List comprehensions), сформируйте следующие списки из указанных объектов:

lst_animals - все объекты, относящиеся к животным (Animals);
lst_plants - все объекты, относящиеся к растениям (Plants);
lst_mammals - все объекты, относящиеся к млекопитающим (Mammals).
'''

class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


input_lst = '''Monkey: "мартышка", 30.4, 7
Monkey: "шимпанзе", 24.6, 8
Person: "Балакирев", 88, 34
Person: "Верховный жрец", 67.5, 45
Flower: "Тюльпан", 0.2, 1
Flower: "Роза", 0.1, 2
Worm: "червь", 0.01, 1
Worm: "червь 2", 0.02, 1'''

lst_objs = []
for elem in input_lst.split('\n'):
    obj, args = elem.split(': ')
    name, weight, old = args.split(', ')
    lst_objs.append(eval(f"{obj}({name}, {weight}, {old})"))

lst_animals = [elem for elem in lst_objs if isinstance(elem, Animals)]
lst_plants = [elem for elem in lst_objs if isinstance(elem, Plants)]
lst_mammals = [elem for elem in lst_objs if isinstance(elem, Mammals)]
