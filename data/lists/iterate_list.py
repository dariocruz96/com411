def directions():
    directions = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please enter a direction:")
    direction = directions()
    for index in range(len(direction)):
        direct = direction[index]
        print(f"{index}: {direct}")


def run():
    menu()


run()
