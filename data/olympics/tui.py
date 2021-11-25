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
    gold = 0
    silver = 0
    bronze = 0
    for medal in tally:
        if "Gold" in medal:
            gold += 1
        elif "Silver" in medal:
            silver += 1
        elif "Bronze" in medal:
            bronze += 1

    output = {"Gold": gold, "Silver": silver, "Bronze": bronze}
    z = ""
    for key, value in output.items():
        print(f"| {key:10}| {value}{z:5}|")
    return output


def display_team_medal_tally(team_tally):
    pass
    teams = team_tally
    output = {}
    gold = 0
    silver = 0
    bronze = 0
    for i in range(len(teams)):
        for j in range(len(teams)):
            if teams[i] == team_tally[j]:
                if "Gold" in teams[j]:
                    gold += 1
                elif "Silver" in teams[j]:
                    silver += 1
                elif "Bronze" in teams[j]:
                    bronze += 1
                # output.add("{teams[i]}\nGold: {gold}, Silver: {silver}, Bronze: {bronze}}}")
            output[teams[i]].append("{teams[i]}\nGold: {gold}, Silver: {silver}, Bronze: {bronze}}}")
    print(output)

def display_years(years):
    output = set()
    for row in range(len(years)):
        output.add(int(years[row][9]))
    years_reversed = list(output)
    output = sorted(years_reversed, reverse=True)
    print(*output, sep="\n")


def menu():
    selection = input("\n\t[years]\t\tList unique years\n"
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