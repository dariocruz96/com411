print("Program Started!")
code = abs(int(input("Please enter a ASCII code:\n")))
if 32 <= code <= 126:
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is: {character}.")
else:
    print("Please enter a valid ASCII code next time!")
print("Program Ended!")