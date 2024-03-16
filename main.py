'''
main.py. This is where all interactions and functions occur.

--// Class functions //--

--// Other functions //--

main():
- start the program
'''

class Account:
    # Initialize everything
    def __init__(self, _accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self._accountNumber = _accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance
    
    def getAccountNumber():
        pass

    def getAccountHolderName():
        pass

    def getRateOfInterest():
        pass

    def getCurrentBalance():
        pass

    def deposit():
        pass

    def withdraw():
        pass

class SavingsAccount(Account):
    pass

class ChequingAccount(Account):
    pass

class Bank:
    pass

class Program:
    # Main menu screen
    def showMainMenu(self):
        while True:
            print("\nMain Menu:")
            print("1. Select Account")
            print("2. Exit")

            choice = input("Enter your choice: ")

            # Select Account menu
            if choice == "1":
                account_number = input("Enter account number: ")
                self.showAccountMenu()
            # Exit the app
            elif choice == "2":
                print("Exiting the application...")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice. Please try again.")

    # Account menu screen
    def showAccountMenu(self):
        while True:
            print("\nAccount:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Check balance
                pass
            elif choice == "2":
                # Desposit
                pass
            elif choice == "3":
                # Withdraw
                pass
            elif choice == "4":
                # Exit the account menu
                break

    def run(self):
        self.showMainMenu()

def main():
    # create the program class and start it
    program = Program()
    program.run()

# Main function to run the program
main()
