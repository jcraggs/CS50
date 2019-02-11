"""A program which builds a staircase made of #'s with the size dependent on user input"""
def main():
    """Main program"""
    val = user_inputs()
    print_staircase(val)


def user_inputs():
    """This function gets the user inputs"""
    while True:
        user_input = input(
            "How tall do you want Mario's staircase? (Enter a number between 1 - 8): ")
        try:
            val = int(user_input)
            if val > 8 or val < 1:
                print("Error_1: Number must be between 1-8 \n")
            if 1 <= val <= 9:
                break
        except ValueError:
            print("Error_2: Input must be a number between 1-8 \n")
    return val


def print_staircase(val):
    """This function prints the staircase of #'s"""
    rolling_number = 0
    rolling_reverse = val
    space_var = " "
    hash_var = "#"

    while rolling_number < val+1:
        print(" "+(rolling_reverse)*space_var + (1*hash_var)*rolling_number)
        rolling_number += 1
        rolling_reverse -= 1
    print()


if __name__ == "__main__":
    main()
