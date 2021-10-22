def run():
    def display_box(name):
        message = f"* Hello {name} *"
        print("*" * len(message))
        print(message)
        print("*" * len(message))

    def greet_user(username):
        print(f"Hello {username}.")

    def upper(name):
        text = name.upper()
        print(text)

    def lower(name):
        text = name.lower()
        print(text)

    def backwords(name):
        return name[::-1]

    print("Please enter your name")
    name = input()
    greet_user(name)

    print("Please choose an option:")
    print("1) Display in a Box – display the word in an ascii art box")
    print("2) Display Lower-case – display the word in lower-case e.g. hello")
    print("3) Display Upper-case – display the word in upper-case e.g. HELLO")
    print("4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH")
    print("5) Repeat – ask the user how many times to display the word and then display the word that many times "
          "alternating between upper-case and lower-case.")
    option = int(input())

    if option == 1:
        display_box(name)
    elif option == 2:
        lower(name)
    elif option == 3:
        upper(name)
    elif option == 4:
        text = backwords(name)
        print(text)
    elif option == 5:
        count = 0
        times = int(input("How many times do you want to display your name?"))
        while count < times:
            if count % 2 == 0:
                upper(name)
                count += 1
            elif count % 2 == 1:
                lower(name)
                count += 1


if __name__ == "__main__":
    run()
