import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        heading = next(csv_reader)
        headings.append(heading)
        for values in csv_reader:
            records.append(values)
    print("Done!")


def display_menu():
    print("Please select one of the following options:\n"
          "[1] Display the names of all passengers\n"
          "[2] Display the number of passengers that survived\n"
          "[3] Display the number of passengers per gender\n"
          "[4] Display the number of passengers per age group\n")
    while True:
        choice = int(input())
        if 4 < choice:
            print("Sorry, that option is not valid.")
            continue
        else:
            break
    return choice


def display_passenger_names():
    print("The names of the passengers are...\n")
    for names in records:
        passenger_name = names[3]
        print(passenger_name)


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.\n")
    selected_option = display_menu()
    print(f"You have selection option: {selected_option}\n")
    if selected_option != 1:
        print("Error! Option not recognised!")
    else:
        display_passenger_names()


if __name__ == "__main__":
    run()
