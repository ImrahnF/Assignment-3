class Account:
    # Initialize everything
    def __init__(self, _accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self._accountNumber = _accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance

    def getAccountNumber(self):
        return self._accountNumber

    def getAccountHolderName(self):
        return self._accountHolderName

    def getRateOfInterest(self):
        return self._rateOfInterest

    def getCurrentBalance(self):
        return self._currentBalance

    def deposit(self, amount):
        self._currentBalance += amount

    def withdraw(self, amount):
        self._currentBalance -= amount

class SavingsAccount(Account):
    pass

class ChequingAccount(Account):
    pass

class Bank:
    # Start with an empty database that will house all the accounts
    def __init__(self):
        self.accounts = []

    # Search self.accounts given an account number. If it exists, return it
    def searchAccount(self, account_number):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                return account
        return None

class Program:
    # Establish a connection with the bank so that we can access it 
    def __init__(self, bank):
        self.bank = bank

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
                account = self.bank.searchAccount(account_number)
                if account:
                    self.showAccountMenu(account)
                else:
                    print("Account not found.")
            # Exit the loop and end the program
            elif choice == "2":
                print("Exiting the application...")
                break  
            # There was an invalid input so just try again
            else:
                print("Invalid choice. Please try again.")

    # Account menu screen
    def showAccountMenu(self, account):
        while True:
            print("\nAccount:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Current Balance:", account.getCurrentBalance())
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                print("Deposit successful. Current Balance:", account.getCurrentBalance())
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                print("Withdrawal successful. Current Balance:", account.getCurrentBalance())
            elif choice == "4":
                break  # Exit the account menu

    def run(self):
        self.showMainMenu()

def main():
    chequing = Account("123", "John Doe", 0.05, 1000)
    
    bank = Bank()
    bank.accounts.append(chequing)
    program = Program(bank)
    program.run()

# Main function to run the program
main()