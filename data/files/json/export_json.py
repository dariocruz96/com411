import json


def read(filePath):
    print("Reading...Done!")
    with open(filePath) as file:
        data = json.load(file)
    return data


def save(newfilePath, data):
    print("Exporting...Done!")
    with open(newfilePath, "w") as file:
        json.dump(data, file, indent=4)


def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run()
