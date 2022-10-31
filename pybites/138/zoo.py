class Animal:

    counter = 10_000
    animals = []

    def __init__(self, name):
        self.name = name.title()
        Animal.counter += 1
        self.id = Animal.counter
        Animal.animals.append(self)

    def __str__(self):
        return f"{self.id}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join(str(animal) for animal in cls.animals)
