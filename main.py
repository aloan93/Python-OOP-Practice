from bank_accounts import *

Jeff = BankAccount(500, "Jeff's nest egg")
Holly = BankAccount(25, "Holly's change horde")

print(f'\n{Jeff.name}')

Jeff.name = "Jeff's NEW nest egg"
print(f'\n{Jeff.name}')

Holly.deposit(50)

Holly.withdraw(50)
Holly.withdraw(10.5)

Jeff.transfer(1000, Holly)
Jeff.transfer(100, Holly)