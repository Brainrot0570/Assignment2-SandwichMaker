class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int(input("How many dollars?: "))
        half_dollars = int(input("How many half dollars?: ")) * .5
        quarters = int(input("How many quarters?: ")) *.25
        nickels = int(input("How many nickels?: ")) * .05
        return large_dollars + half_dollars + quarters + nickels
        ###

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        change = coins - cost
        print(f"Here is ${change} in change.")
        return True
        ##
