def run():
    number = int(input("Please enter a whole number.\n"))

    if number % 2 == 1:
        print("The number", number, "is an odd number")
    elif number % 2 == 0:
        print("The number", number, "is an even number")


if __name__ == "__main__":
    run()
