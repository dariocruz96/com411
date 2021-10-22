def run():
    book = input("What type of book is this?(adventure, horror, comedy, action)")

    if book == "adventure":
        print("I like adventure books!")
    elif book == "horror":
        print("I like horror books!")
    elif book == "comedy":
        print("I like comedy books!")
    elif book == "action":
        print("I like action books!")

    print("Finished reading book.")


if __name__ == "__main__":
    run()
