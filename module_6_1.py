class Animal:
    alive = True
    fed = False
    name = []

    def __new__(cls, *args, **kwargs):
        cls.name.append(0)
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False
    name = []

    def __new__(cls, *args, **kwargs):
        cls.name.append(0)
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food == p1:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        else:
            print(f'{self.name} съел {food.name}')
            self.fed = True


class Predator(Animal):
    def eat(self, food):
        if food == p1:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        else:
            print(f'{self.name} съел {food.name}')
            self.fed = True


class Flower(Plant):
    pass


class Fruit(Plant):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
