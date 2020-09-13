# This will compute the percent of increase in positive cases of covid19 positive

def computeIncrease(old_case, new_case):
    return old_case * (new_case / 100)


def start():
    try:
        old_case = int(input("Enter the number of old cases: "))
        new_case = int(input("Enter the number of new cases: "))
        print("There is a " + str(computeIncrease(old_case, new_case)) + "% increase of infected.")
    except:
        # add specific error for input error
        print("Invalid Input. Enter valid data.")
        start()


start()

