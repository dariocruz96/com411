class Planet:
    def __init__(self):
        self.humans = []
        self.robots = []

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)

    # Magic methods
    def __repr__(self):
        return f'Humans={self.humans}, Robots={self.robots}'

    def __str__(self):
        return f'Humans={self.humans}, Robots={self.robots}.'


if __name__ == "__main__":
    planet = Planet()
    planet.add_human("Dario")
    planet.add_robot("Tiago")

    print(planet)
