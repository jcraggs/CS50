"""A program which calculates the change for a purchase dependent on user input"""
def main():
    """Main program"""
    denominations, local_crncy = currency_denom()
    cost = cost_input(local_crncy)
    paid = paid_input(cost, local_crncy)
    rcv = change_req(cost, paid, local_crncy)
    smallest_change(rcv, local_crncy, denominations)


def currency_denom():
    """Allows code to be edited to suit different currency denominations"""
    denominations = sorted([50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]) #edit this to change denominations
    local_crncy = "£" #edit this depending on currency

    return denominations, local_crncy


def cost_input(local_crncy):
    """Getting the user to input the cost of the item"""
    while True:
        try:
            cost = float(input(
                "How much does the item cost (enter value as a number with decimals i.e 3.99 for "+ local_crncy +"3.99)?: "))
            if cost < 0 or cost == 0:
                print("Error_1: Cost must be entered as a number greater than 0 \n")
            if cost > 0:
                break
        except ValueError:
            print("Error_3: Cost must be entered as a number \n")

    return cost


def paid_input(cost, local_crncy):
    """Getting the user to input how much the customer has paid for the item"""
    while True:
        try:
            paid = float(input(
                "How much has the customer paid (enter value as a number with decimals i.e 3.99 for "+ local_crncy+ "3.99)?: "))
            if paid < cost:
                print("Error_1: Payment must be greater than the cost of the item \n")
            if paid > cost or paid == cost:
                break
        except ValueError:
            print("Error_2: Payment must be entered as a number \n")

    return paid


def change_req(cost, paid, local_crncy):
    """Displaying the amount of change the customer requires"""
    change_val = (paid - cost)
    rcv = round(change_val, 2)
    if rcv == 0:
        print("\nThe customer does not require change.")
        exit()
    if rcv > 0:
        print("\nThe customer is owed: "+ local_crncy + str(rcv))

    return rcv


def smallest_change(rcv, local_crncy, denominations):
    """Calculating and displaying the fewest denominations required to give the customer their change"""
    print("\nYou need to give the customer the following change denominations: \n")

    denominations.reverse()

    while rcv > 0:
        for i in denominations:
            if i <= rcv:
                divid_change = rcv/i
                whole_change = int(divid_change)
                print("- " + local_crncy + str(i) + " x " + str(whole_change))
                rcv = round(((divid_change-whole_change)*i), 2)


if __name__ == "__main__":
    main()
