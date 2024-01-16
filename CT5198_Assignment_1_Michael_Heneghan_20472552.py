# Michael Heneghan 20472552
# Creating a main function to store my list
def main():
    # Part (A)
    # making my customer list which will store the inputs given
    customer_list = []
    # Part (B)
    # creating a for loop here in the range 1-8 as there is 7 days in the week
    for day in range(1, 8):
        # while statement so the loop runs while the day is between 1 and 7
        while True:
            try:
                # declaring the input must be of type int
                customers = int(input("Enter number of customers for the day:"))
                # here I am appending any days with 0 or more customers to my original list
                if customers >= 0:
                    customer_list.append(customers)
                    break
                # Conditional possibilities to be considered like someone entering letters or negative numbers
                # else clause will deny negative numbers
                # ValueError will stop letters
                else:
                    print("Invalid input: Please enter a positive integer")
            except ValueError:
                print("Invalid input please enter a valid digit")

    # Part (C)
    # finding min, max and avg using min, max methods and sum divided by len method
    if customer_list:
        customer_max = max(customer_list)
        customer_min = min(customer_list)
        customer_avg = sum(customer_list)/len(customer_list)

        # printing out results below
        print("The most amount customers we had in a day was", customer_max)
        print("The least amount of customers we had in a day is", customer_min)
        # using built in round() function to round up to next integer as you cant round down when dealing with people
        print("The avg amount of customers we had this week is", round(customer_avg))


main()