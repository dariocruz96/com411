def run():
    def listen():
        print(f"That was a loud {word}!")

    word = input("What sound did I hear?\n")

    listen()


if __name__ == "__main__":
    run()
