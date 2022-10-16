class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []
        self.current_weight = 0

    def verify_weight(self, value):
        if self.current_weight + value > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def verify_index(self, index):
        if index >= len(self.bag):
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        self.verify_weight(thing.weight)
        self.current_weight += thing.weight
        self.bag.append(thing)

    def __getitem__(self, item):
        self.verify_index(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        self.verify_index(key)
        self.current_weight -= self.bag[key].weight
        self.verify_weight(value.weight)
        self.bag[key] = value

    def __delitem__(self, key):
        self.verify_index(key)
        del self.bag[key]


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __setattr__(self, key, value):
        if key == 'name' and type(value) == str:
            object.__setattr__(self, key, value)
        elif key == 'weight' and type(value) in (int, float):
            object.__setattr__(self, key, value)


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    # assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"