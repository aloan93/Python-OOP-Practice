class BankAccount:
    def __init__(self, initial_ammount, account_name):
        self.balance = initial_ammount
        self.__name = account_name
        print(f"\nAccount '{self.name}' created\nBalance = £{self.balance:.2f}")
    
    @property
    def name(self):
        return(self.__name)
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
            print(f"\nName of account successfully changed to '{self.__name}'")
        else:
            print("\nRename failed\nAccount names must be of type 'string'")