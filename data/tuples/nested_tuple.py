def steps():
    likelihoods = (("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4))
    return likelihoods


def run():
    value = steps()
    good_steps = []
    bad_steps = []
    for step in value:
        if step[1] >= 50:
            bad_steps.append(step[0][-2:])
        else:
            good_steps.append(step[0][-2:])
    separator = ", "
    print(f"Good steps: {separator.join(good_steps)}, Bad steps: {separator.join(bad_steps)}")


if __name__ == "__main__":
    run()
