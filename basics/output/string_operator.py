def run():
    lives = int(input("Please enter the number of lives. "))
    energy = int(input("Please enter the energy level. "))
    shield = int(input("Please enter the shield level. "))

    print("Health has been set.")

    print("Lives:  " + "\u2764" * lives)
    print("Energy: " + "\u2742" * energy)
    print("Shield: " + "\u2756" * shield)


if __name__ == "__main__":
    run()