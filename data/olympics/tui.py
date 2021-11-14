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


def menu():
    selection = input("\n\t[years]\t\tList unique_years\n"
                      "\t[tally]\t\tTally up medals\n"
                      "\t[team]\t\tTally up medals for each team\n"
                      "\t[exit]\t\tExit the program\n")
    return selection


def display_medal_tally(tally):
    print(f"{tally[gold]}")
    return tally


started("Reading data from athlete_events.csv...")
completed()
error("Invalid Selection!")
menu()
