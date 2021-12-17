import matplotlib.pyplot as plt
import random as rnd

#n = random.random()


def data():
    paths = {}
    line_style = input("What type of line would you like (- or --)?")
    colour = input("What colour would you like (r,g or b)?")
    marker_style = input("What style of marker would you like(o, s or ^)?")
    paths['line_style'] = line_style
    paths['colour'] = colour
    paths['marker_style'] = marker_style
    return paths


def generate():
    num_lines = int(input("How many lines would you like to display? "))
    for num_line in range(num_lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        plt.plot(x, y, format)


def run():
    print("Running...")
    generate()
    plt.show()
    print("Done!")


run()
