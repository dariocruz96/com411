from random import randrange

min_num = int(input("Please enter the minimum value:\n"))
max_num = int(input("Please enter the maximum value:\n"))

guess = int(input(f"I am thinking of a number between {min_num} and {max_num}. Can you guess what it is?\n"))

number = randrange(min_num, max_num, 1)
while guess != number:
    if guess > number:
        print("Your guess is too high.")
        guess = int(input("Try again:\n"))
    elif guess < number:
        print("Your guess is too low.")
        guess = int(input("Try again:\n"))

print("Congratulations! You guessed my number!")