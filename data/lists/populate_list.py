def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    direction = directions()
    for index in range(len(direction)):
        direct = direction[index]
        print(f"{index}: {direct}")
    while True:
        choice = int(input())
        if choice > len(direction):
            print("Sorry, that option is not valid.")
            continue
        else:
            break
    return direction[choice]


def run():
    route = []
    print("Working out escape route...")
    for i in range(5):
        route.append(menu())

    print(f"Escape route: {route}")


run()
