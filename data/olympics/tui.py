def started(msg=""):
    for i in range(85):
        print("-", end="")
    if msg != "":
        print(f"\nOperation started: {msg}")


def completed():
    print("\nOperation completed.")
    started("")


def error(msg=""):
    print(f"\nError! {msg}")


def display_medal_tally(tally):
    # tally = {"Gold": 14142, "Silver": 12323, "Bronze": 11111}
    # print(gold : tally.count("gold"))
    z = ""
    for key, value in tally.items():
        print(f"| {key:10}| {value}{z:5}|")


def display_team_medal_tally(team_tally):
    tally = {"Gold": 14142, "Silver": 12323, "Bronze": 11111}
    team_tally = {"Team name": tally}

    for key, value in team_tally.items():
        print(f"{key}\n\t{value}")


def display_years(years):
    print(years.sort(reverse=True))


def menu():
    selection = input("\n\t[years]\t\tList unique_years\n"
                      "\t[tally]\t\tTally up medals\n"
                      "\t[team]\t\tTally up medals for each team\n"
                      "\t[exit]\t\tExit the program\n")
    return selection


def run():
    started("Reading data from athlete_events.csv...")
    completed()
    error("Invalid Selection!")
    menu()
    display_medal_tally()
    display_team_medal_tally()


if __name__ == "__main__":
    run()