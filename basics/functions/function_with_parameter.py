def run():
    def escape_by(plan):
        if plan == "jumping over":
            print("We cannot escape that way! The boulder is to big!")
        elif plan == "running arround":
            print("We cannot escape that way! The boulder is moving too fast!")
        elif plan == "going deeper":
            print("That might work! Let's go deeper")
        else:
            print("We cannot escape that way! The boulder is in the way!")

    escape_by("jumping over")
    escape_by("running around")
    escape_by("going deeper")


if __name__ == "__main__":
    run()
