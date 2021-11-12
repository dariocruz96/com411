def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run():
    print("Analysing patterns...")
    short = short_pattern()
    medium = medium_pattern()
    long = long_pattern()
    pattern = {"Short sequence": short,
               "Medium sequence": medium,
               "Long sequence": long}

    for key, value in pattern.items():
        print(f"{key}: {value}")


run()
