class Robot:
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0):
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY

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
        return f'robot(name={self.name}, age={self.age}, energy={self.energy}'

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

    def display(self):
        print(f"I am {self.name}")


if (__name__ == "__main__"):
    robot = Robot()
    robot.display()
    robot.grow()
    robot.eat(-10)
    robot.eat(-10)
    print(robot)