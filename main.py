from bank_accounts import *

Jeff = BankAccount(500, "Jeff's nest egg")
Holly = BankAccount(25, "Holly's change horde")

print(f'\n{Jeff.name}')
Jeff.name = 'This is a new name'
print(f'\n{Jeff.name}')
Jeff.name = 000