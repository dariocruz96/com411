def run():
    firstNumber = int(input("Please enter the first number.\n"))
    secondNumber = int(input("Please enter the second number.\n"))

    if firstNumber > secondNumber:
        print("The second number is the smallest.")
    elif secondNumber > firstNumber:
        print("The first number is the smallest.")
    else:
        print("They are equal.")


if __name__ == "__main__":
    run()
