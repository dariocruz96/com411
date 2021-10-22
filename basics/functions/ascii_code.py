def run():
    print("Program Started!")
    letter = input("Please enter a letter:\n")
    if len(letter) == 1:
        value = ord(letter)
        print(f"The ASCII code for {letter} is: {value}.")
    else:
        print("Please enter just one letter next time!")
    print("Program Ended!")


if __name__ == "__main__":
    run()
