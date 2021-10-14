def display_ladder(steps_inp):
    print("| |")
    for i in range(steps_inp):
        print("***\n| |")


def create_ladder():
    steps = int(input("How many steps remain?\n"))
    display_ladder(steps)


create_ladder()
