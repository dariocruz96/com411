def run():
    def identify():
        word = input("Please type a word representing what you see:\n")
        if word == "a large boulder":
            print("It's time to run!")
        else:
            print("We will be fine.")

    identify()


if __name__ == "__main__":
    run()
