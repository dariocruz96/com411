def run():
    firstNumber = int(input("Please enter the first whole number.\n"))
    secondNumber = int(input("Please enter the second whole number.\n"))
    thirdNumber = int(input("Please enter the third whole number.\n"))
    even = 0
    odd = 0
    if firstNumber % 2 == 0:
        even += 1
    elif firstNumber % 2 == 1:
        odd += 1

    if secondNumber % 2 == 0:
        even += 1
    elif secondNumber % 2 == 1:
        odd += 1

    if thirdNumber % 2 == 0:
        even += 1
    elif thirdNumber % 2 == 1:
        odd += 1

    print("There were", even, "even and", odd, "numbers.")

if __name__ == "__main__":
    run()