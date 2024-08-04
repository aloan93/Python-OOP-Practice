class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_ammount, account_name):
        self.__balance = initial_ammount
        self.__name = account_name
        print(f"\nAccount '{self.name}' created\nBalance = £{self.__balance:.2f}")
    
    @property
    def name(self):
        return(self.__name)
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        print(f"\nName of account successfully changed to '{self.__name}'")

    def show_balance(self):
        print(f"\nAccount '{self.__name}'\nBalance = £{self.__balance:.2f}")

    def deposit(self, ammount):
        self.__balance += ammount
        print(f"\nDeposit successful")
        self.show_balance()

    def viable_transaction(self, ammount):
        if self.__balance >= ammount:
            return
        else:
            raise BalanceException(f"\nAccount '{self.__name}' lacks suffcient funds - Current balance £{self.__balance:.2f}")
        
    def withdraw(self, ammount):
        try:
            self.viable_transaction(ammount)
            self.__balance -= ammount
            print("\nTransaction successful")
            self.show_balance()
        except BalanceException as error:
            print(f"\nTransaction failed: {error}")

    def transfer(self, ammount, account):
        try:
            print("\n**********\n\nBeginning Transfer...")
            self.viable_transaction(ammount)
            self.withdraw(ammount)
            account.deposit(ammount)
            print("Transfer Complete!\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer failed: {error}")