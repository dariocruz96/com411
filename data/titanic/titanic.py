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


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")


if __name__ == "__main__":
    run()
