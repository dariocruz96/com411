def search(fileName):
    with open(fileName) as file:
        print("Searching...")
        for line in file:
            print(f"Looked in the {line.strip()}.")
    print("...Done!")


def run(fileName):
    search(fileName)


if __name__ == "__main__":
    run("library.txt")