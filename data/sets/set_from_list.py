def observed():
    observations = []
    for index in range(7):
        user_input = input("Please enter an observation:")
        observations.append(user_input)
    return observations


def run():
    print("Counting observations...")
    my_list = observed()
    my_set = set()
    for element in my_list:
        my_set.add((element, my_list.count(element)))
        # print((element, my_list.count(element)))
    for element in list(my_set):
        print(f"{element[0]} observed {element[1]} time(s).")


run()
