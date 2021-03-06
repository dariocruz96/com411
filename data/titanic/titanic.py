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
          "[4] Display the number of passengers per age group\n"
          "[5] Display the number of survivors per age group\n")
    choice = int(input())
    return choice


def display_passengers_names():
    print("The names of the passengers are...\n")
    for passenger in records:
        passenger_name = passenger[3]
        print(passenger_name)


def display_number_survivors():
    num_survived = 0
    for passenger in records:
        survival_status = int(passenger[1])
        if survival_status == 1:
            num_survived += 1
    print(f"{num_survived} passengers survived.")
    return num_survived


def display_passengers_per_gender():
    females = 0
    males = 0
    for passenger in records:
        gender = passenger[4]
        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1
    print(f"females: {females}, males: {males}")


def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for passenger in records:
        if passenger[5] != "":
            age = float(passenger[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    return children, adults, elderly


def display_survivors_per_age_group():
    passengers_per_age_group = display_passengers_per_age_group()
    children_surv = 0
    adults_surv = 0
    elderly_surv = 0
    for passenger in records:
        if passenger[5] != "":
            age = float(passenger[5])
            survived = int(passenger[1])
            if age < 18 and survived == 1:
                children_surv += 1
            elif age < 65 and survived == 1:
                adults_surv += 1
            elif age >= 65 and survived == 1:
                elderly_surv += 1
    print(f"children: {children_surv}/{passengers_per_age_group[0]}, "
          f"adults: {adults_surv}/{passengers_per_age_group[1]}, "
          f"elderly: {elderly_surv}/{passengers_per_age_group[2]}")




def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.\n")
    selected_option = display_menu()
    print(f"You have selection option: {selected_option}\n")
    if selected_option == 1:
        display_passengers_names()
    elif selected_option == 2:
        display_number_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        age = display_passengers_per_age_group()
        print(f"children: {age[0]}, adults: {age[1]}, elderly: {age[2]}")
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()
