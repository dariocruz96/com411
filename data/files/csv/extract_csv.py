import csv


def read(filepath):
    print("Extracting...", end="")
    print("The extracted names are:")
    with open("bots.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            # display only the names
            print(values[1])
    print("Done!")


def run():
    read("bots.csv")


if __name__ == "__main__":
    run()
