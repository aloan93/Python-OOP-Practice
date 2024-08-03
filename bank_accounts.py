class BankAccount:
    def __init__(self, initial_ammount, account_name):
        self.balance = initial_ammount
        self.name = account_name
        print(f"\nAccount '{self.name}' created\nBalance = £{self.balance:.2f}")