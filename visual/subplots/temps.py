import matplotlib.pyplot as plt


def read_data(filepath):
    my_list = []
    with open(filepath) as file:
        for line in file:
            my_list.append(int(line.strip()))
    return my_list

def run():
    data = read_data("temps.txt")
    fig, axs = plt.subplots(1, 2, sharey="row")
    # days to show in x-axis
    days = range(1, 8)
    # plot line and bar chart
    axs[0].plot(days, data)
    axs[1].bar(days, data)

    # set x limits to show all days
    axs[0].set_xlim(min(days), max(days))
    axs[1].set_xlim(min(days), max(days))

    # add labels
    axs[0].set_xlabel('Day')
    axs[0].set_ylabel('Temperature')
    axs[1].set_xlabel('Day')
    plt.tight_layout()
    plt.show()
run()