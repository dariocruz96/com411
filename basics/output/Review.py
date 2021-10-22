def run():
    name = input("What is your name human? ")
    print("Hello", name, "here is your journey friend:")
    print("             |\___/|")
    print("            (,\  /,))")
    print("            /     / )")
    print("           (@_^_@)/   )")
    print("            W//W_/ )")
    print("          (//) |        )")
    print("       (/ /) _|_ /   ) )")
    print("      (// /) '/,_ _ _/  (~^-.")
    print("    (( // )) ,-{        _    `.")
    print("   (( /// ))  '/\      /      |")
    print("   (( ///))     `.   {       }")
    print("    ((/ ))    .----~-.\   \-'")
    print("             ///.----..>   )")
    print("              ///-._ _  _ _}")
    print("He will be responsible for your safety in this battle that you are about to enter!")
    print("Your current status are: ")
    print("Lives:  " + "\u2764" * 5)
    print("Energy: " + "\u2742" * 5)
    print("Shield: " + "\u2756" * 5)

    path = input("Would you like to fight a dragon or a bee? ")
    if path == "dragon":
        print(
            "Oh no, the dragon seems to be bigger than a mountain and your friend dies while saving you from certain death!")
        print("Your current status are: ")
        print("Lives:  " + "\u2764" * 3)
        print("Energy: " + "\u2742" * 1)
        print("Shield: " + "\u2756" * 0)

    elif path == "bee":
        print("The bee seems really sweet! Why would you...OH NOT, A BEE ARMY APPEARED!! RUUUUUUUUN!")
        print("Your current status are: ")
        print("Lives:  " + "\u2764" * 4)
        print("Energy: " + "\u2742" * 2)
        print("Shield: " + "\u2756" * 1)

    secondPath = input("What should we do now? Try again or run? ")

    if secondPath == "try again":
        print("YOU DID IT! Congratulations!! You are the best warrior of the kingdom!")
        print("Your current status are: ")
        print("Lives:  " + "\u2764" * 1)
        print("Energy: " + "\u2742" * 0)
        print("Shield: " + "\u2756" * 0)

    elif secondPath == "run":
        print(
            "You were able to run away, but...what a disgrace you are to your people...Enjoy the rest of your life, you scary fish!")

    if __name__ == "__main__":
        run()
