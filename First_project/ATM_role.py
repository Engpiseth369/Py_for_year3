class ATM:

    def __init__(self):
        # Default variables
        self.balance = 40000

        self.cash = {100: 50, 50: 20, 20: 300, 10: 0, 5: 200, 1: 10}

    # Withdrawal method
    def withdraw(self, amount):
        try:

            if amount <= 0:
                print("Invalid amount!")
                return

            elif amount > self.balance:
                print("Insufficient balance!")
                return

            total_cash = sum(
                denomination * quantity for denomination, quantity in self.cash.items()
            )

            if amount > total_cash:
                print("Sorry! The ATM has insufficient cash.")
                return

        except ValueError:
            print("Invalid input! Please enter a valid number.")

        remaining = amount
        withdrawn = {}

        # Calculate banknotes
        for denomination, quantity in self.cash.items():

            count = min(remaining // denomination, quantity)

            withdrawn[denomination] = count
            remaining -= count * denomination

        # Check available ATM cash
        if remaining > 0:
            print("ATM does not have enough cash!")
            return

        # Update ATM cash
        for denomination, count in withdrawn.items():
            self.cash[denomination] -= count

        # Update account balance
        self.balance -= amount

        print("\n===== WITHDRAWAL SUCCESS =====")
        print(f"\n\tWithdrawn: ${amount}")

        print("\tYou have received: ")
        for denomination, count in withdrawn.items():
            if count > 0:
                print(f"\t\t${denomination} x {count}")

        print(f"\tRemaining Balance: ${self.balance}")


# Create ATM object
atm = ATM()
a = int(input("Enter amount: "))
# Run ATM
# atm.menu()
atm.withdraw(a)
