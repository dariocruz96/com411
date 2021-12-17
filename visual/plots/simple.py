import matplotlib.pyplot as plt

x = [0, 5, 10]
y = [0, 50, 100]

plt.plot(x, y)
plt.show()


def display(x_list, y_list):
    plt.plot(x_list, y_list)
    plt.show()


def run():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display(x_values, y_values)

run()