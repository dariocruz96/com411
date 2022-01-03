from random import randint
from planet import Planet
from robot import Robot
from human import Human


class Universe:
    def __init__(self):
        self.planets = []

    def __repr__(self):
        return f"universe(planets={self.planets})"

    def __str__(self):
        return f"The Universe contains {len(self.planets)} planets."

    def generate(self):
        planet = Planet()
        for index in range(randint(0, 10)):
            robot = Robot(f'Robot {index}')
            planet.add_robot(robot)

        for index in range(randint(0, 10)):
            human = Human(f'Human {index}')
            planet.add_human(human)

        self.planets.append(planet)


if __name__ == "__main__":
    universe = Universe()
    universe.generate()
    print(universe)
