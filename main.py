from bank_accounts import *

Jeff = InterestRewardsAccount(500, "Jeff's nest egg")
Holly = BankAccount(25, "Holly's change horde")

print(f'\n{Jeff.name}')

Jeff.name = "Jeff's NEW nest egg"
print(f'\n{Jeff.name}')

Holly.deposit(50)

Holly.withdraw(50)
Holly.withdraw(10.5)

Jeff.deposit(100)

Jeff.transfer(1000, Holly)
Jeff.transfer(100, Holly)

Charlie = SavingsAccount(100, "Charles' Student Debt")

Charlie.withdraw(100)
Charlie.withdraw(50)
Charlie.deposit(50)