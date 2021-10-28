def export(filePath, numberBots):
    print("Exporting...")
    with open(filePath, "a") as file:
        for bot in range(numberBots):
            bot_id = input("Enter bot id:\n")
            bot_name = input("Enter bot name:\n")
            bot_paint = input("Enter the bot paint:\n")
            file.write(f"\n{bot_id},{bot_name},{bot_paint}")
    print("Done!")


export("exported_bots.csv", 2)