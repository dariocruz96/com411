import matplotlib.pyplot as plt


def coordinate():
    x = int(input("Enter an x value: "))
    y = int(input("Enter an y value: "))
    return x, y


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return x_values, y_values


def run():
    values = path()
    plt.plot(values[0], values[1], "ro--")
    plt.show()
run()
