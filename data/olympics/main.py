import csv
# import process
import tui
import data.olympics.tui as started


def read_data(file_path):
    tui.started(file_path)
    data = []
    gold = 0
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        for values in csv_reader:
            data.append(values)
            if "Gold" in values:
                gold += 1
    print(gold)
    return data


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            pass
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
