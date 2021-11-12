def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def display_keys(data):
    print("\nKeys:")
    for key in data:
        print(key)


def display_values(data):
    print("\nValues:")
    for value in data.values():
        print(value)


def display_item(data):
    print("\nPairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    output = pattern()
    print(output)
    display_keys(output)
    display_values(output)
    display_item(output)


run()
