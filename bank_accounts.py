class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, account_name):
        self._balance = initial_amount
        self._name = account_name
        print(f"\nAccount '{self.name}' created\nBalance = £{self._balance:.2f}")
    
    @property
    def name(self):
        return(self._name)
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        print(f"\nName of account successfully changed to '{self._name}'")

    def show_balance(self):
        print(f"\nAccount '{self._name}'\nBalance = £{self._balance:.2f}")

    def deposit(self, amount):
        self._balance += amount
        print(f"\nDeposit successful")
        self.show_balance()

    def viable_transaction(self, amount):
        if self._balance >= amount:
            return
        else:
            raise BalanceException(f"\nAccount '{self._name}' lacks suffcient funds - Current balance £{self._balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self._balance -= amount
            print("\nTransaction successful")
            self.show_balance()
        except BalanceException as error:
            print(f"\nTransaction failed: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer...")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer Complete!\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer failed: {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount * 1.05
        print(f"\nDeposit successful")
        self.show_balance()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self._balance -= amount + self.fee
            print("\nTransaction successful")
            self.show_balance()
        except BalanceException as error:
            print(f"\nTransaction failed: {error}")