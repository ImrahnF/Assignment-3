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
    pass

class Program:
    # Main menu screen
    def showMainMenu(self):
        pass

    # Account menu screen
    def showAccountMenu(self, account):
        pass

    def run(self):
        self.showMainMenu()

def main():
    program = Program()
    program.run()

# Main function to run the program
main()