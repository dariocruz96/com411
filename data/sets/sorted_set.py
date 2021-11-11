def observed():
    observations = []
    for index in range(5):
        user_input = input("Please enter an observation:\n")
        observations.append(user_input)
    return observations


def remove_observations(observations):
    while True:
        user_input = input("Do you wish to remove an observation (yes/no)?\n")
        if user_input == "yes":
            user_input = input("What observation do you wish to remove?\n")
            observations.remove(user_input)
        elif user_input == "no":
            break
    return observations


def run():

    my_list = observed()
    final_list = remove_observations(my_list)
    print("Observations:")
    my_set = set()
    for element in final_list:
        my_set.add((element, final_list.count(element)))
        # print((element, my_list.count(element)))
    for element in list(sorted(my_set)):
        print(f"{element[0]} observed {element[1]} time(s).")


run()
