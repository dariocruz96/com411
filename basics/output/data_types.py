name = input("What is your name human? ")
age = int(input("How old are you (in years)? "))
height = float(input("How tall are you (in meters)? "))
height = height * 100
weight = float(input("How much do you weigh (in kilograms)? "))
bmi = weight / height / height * 10000
print(name, "you are ", age, "years old and your bmi is ", bmi)
