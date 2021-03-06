class Human:
    MAX_ENERGY = 100

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100
        elif self.energy < 0:
            self.energy = 0

    # Magic methods
    def __repr__(self):
        return f'human(name={self.name}, age={self.age}, energy={self.energy}'

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

    def display(self):
        print(f"I am {self.name}")



if (__name__ == "__main__"):
    human = Human("Dario")
    human.display()
    human.grow()
    human.eat(-10)

    print(human)
