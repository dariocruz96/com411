import json


def read(filePath):
    print("Reading...", end="")
    with open(filePath) as file:
        data = json.load(file)
    print("Done!")
    return data


def save(newfilePath, data):
    print("Exporting...", end="")
    with open(newfilePath, "w") as file:
        json.dump(data, file, indent=4)
    print("Done!")


def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run()
