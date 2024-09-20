class Animal():
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant():
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):

    def eat(self, food):
        if not food.edible:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
        else:
            print(f"{self.name} съел {food.name}")
            self.fed = True

class Predator(Animal):

    def eat(self, food):
        if not food.edible:
            print(f"{self.name} съел {food.name} и отравился")
            self.alive = False
        else:
            print(f"{self.name} съел {food.name}")
            self.fed = True


class Fruit(Plant):
    edible = True

class Flower(Plant):
    edible = False


animal2 = Predator("Лев")
animal1 = Mammal("Лошадь")
plant1 = Fruit("Персик")
plant2 = Flower("Тысячелистник")

print(animal1.alive)
print(animal1.fed, animal2.fed)

animal1.eat(plant1)
animal2.eat(plant2)

print(animal1.alive, animal2.alive)
print(animal1.fed)
