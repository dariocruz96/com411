def run():
    def sum_weights(weight1, weight2):
        return weight1 + weight2

    def calc_avg_weight(weight1, weight2):
        return sum_weights(weight1, weight2) / 2

    def run2():
        weight1 = int(input("Please enter the weight of Beep:\n"))
        weight2 = int(input("Please enter the weight of Bop:\n"))
        word = input("Sum or average?\n")
        if word == "sum":
            print(f"The sum of Beep and Bop's weight is {sum_weights(weight1, weight2)}")
        elif word == "average":
            print(f"The average of Beep and Bop's weight is {calc_avg_weight(weight1, weight2)}")

    run2()


if __name__ == "__main__":
    run()
