
def get_probs():
    # get all rolls from rolls.dat
    f = open("rolls.dat", "r")
    rolls = f.read().split()
    f.close()

    # count each type of roll with increments as well as total
    counts = [0, 0, 0]
    total_count = len(rolls)

    if total_count == 0:  # avoid divide by 0 error
        return [0, 0, 0]

    for roll in rolls:
        if roll == "R":
            counts[0] += 1
        elif roll == "G":
            counts[1] += 1
        elif roll == "B":
            counts[2] += 1

    # get percent of each type of roll
    ratios = [0.0, 0.0, 0.0]
    for i in range(3):
        ratios[i] = counts[i] / total_count

    # take expected - actual, for each (highest number is recommended)
    expects = [0.47, 0.06, 0.47]
    diffs = [0.0, 0.0, 0.0]

    for i in range(3):
        diffs[i] = expects[i] - ratios[i]

    return diffs


def get_choice():
    probs = get_probs()
    choice_value = max(probs)
    choice_index = probs.index(choice_value)

    if choice_index == 0:
        return "R"
    elif choice_index == 1:
        return "G"
    elif choice_index == 2:
        return "B"
    else:
        return "ERROR IN GET_CHOICE"


def __main__():
    while True:
        choice = get_choice()

        print()
        print("Current Choice: ", choice)
        print("Actual current roll")
        print("- R for red")
        print("- G for green")
        print("- B for black")
        print("- Q for quit")
        roll = input()
        valid_rolls = ["R", "G", "B"]
        roll = roll.upper()  # in case user input is lowercase

        if roll == "Q":
            break  # end control loop
        if roll not in valid_rolls:
            print("Invalid answer, try again.\n")
            continue

        # append this roll to rolls.dat
        with open("rolls.dat", "a") as f:
            f.write(roll + '\n')


__main__()
# __test__()