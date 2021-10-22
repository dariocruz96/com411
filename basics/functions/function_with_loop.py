def run():
    def cross_bridge(steps):
        for i in range(steps):
            print("Crossed step")
        if steps > 5:
            print("The bridge is collapsing!")
        else:
            print("We must keep going!")

    cross_bridge(3)
    cross_bridge(6)


if __name__ == "__main__":
    run()
