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

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder_name, rate_of_interest, current_balance, min_balance):
        super().__init__(account_number, account_holder_name, rate_of_interest, current_balance)
        self._minBalance = min_balance

    def withdraw(self, amount):
        if self._currentBalance - amount < self._minBalance:
            return "Withdrawal rejected. Insufficient funds to maintain minimum balance."
        else:
            self._currentBalance -= amount
            return "Withdrawal successful."

class ChequingAccount(Account):
    def __init__(self, account_number, account_holder_name, rate_of_interest, current_balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, rate_of_interest, current_balance)
        self._overdraftLimit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._currentBalance + self._overdraftLimit:
            return "Withdrawal rejected. Overdraft limit exceeded."
        else:
            self._currentBalance -= amount
            return "Withdrawal successful."

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
    
    def initialize_accounts(self):
        #cCreate 5 different accounts with custom values and add them to the accounts list
        account1 = ChequingAccount("10001", "John Doe", 0.05, 1500, 500)
        account2 = SavingsAccount("10002", "Alice Smith", 0.1, 3000, 500)
        account3 = ChequingAccount("10003", "Bob Johnson", 0.06, 2000, 500)
        account4 = SavingsAccount("10004", "Emma Brown", 0.12, 4000, 500)
        account5 = ChequingAccount("10005", "Michael Wilson", 0.07, 2500, 500)

        # add the accounts
        self.accounts.extend([account1, account2, account3, account4, account5])

class Program:
    # Establish a connection with the bank so that we can access it 
    def __init__(self, bank):
        self.bank = bank
        self.bank.initialize_accounts()

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
                result = account.withdraw(amount)
                print(result, "Current Balance:", account.getCurrentBalance())
            elif choice == "4":
                break  # Exit the account menu

    def run(self):
        self.showMainMenu()

def main():
    bank = Bank()
    bank.initialize_accounts()  # Initialize accounts with hardcoded values
    program = Program(bank)
    program.run()

# Main function to run the program
main()