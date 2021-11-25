import csv
# import process
import tui


def read_data(file_path):
    tui.started(file_path)
    data = []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for values in csv_reader:
            data.append(values)
    return data


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()

        if selection == "years":
            tui.display_years(athlete_data)

        elif selection == "tally":
            tui.display_medal_tally(athlete_data)

        elif selection == "team":
            tui.display_team_medal_tally(athlete_data)

        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
