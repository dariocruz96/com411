import json


def read(filePath):
    with open(filePath) as file:
        data = json.load(file)
        city = data["city"]
        print(f"City name: {city}")
        population = data["population"]
        print(f"Population Size: {population}")
        bots = data["bots"]
        for bot in bots:
            bot_name = bot["name"]
            stats = bot["stats"]
            speed = stats["speed"]
            strength = stats["strength"]
            print(f"{bot_name} has a strength level of {strength} and a speed level of {speed}.")


read("robocity.json")
