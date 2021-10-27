import csv


def read(filepath):
    print("Extracting...Done!")
    print("The extracted names are:")
    with open("bots.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            # display only the names
            print(values[1])


def run():
    read("bots.csv")


if __name__ == "__main__":
    run()
