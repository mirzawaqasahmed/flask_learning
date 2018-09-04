####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account():

    def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

    def __repr__(self):
        return f"Account Holder: {self.owner}\nAccount Balance: ${self.balance}"

    def deposit(self, deposit_amount):
        
        self.balance += deposit_amount
        # return self.balance
        print(f"Your current balance is {self.balance}")

    def withdraw(self, withdraw_amount):
        # self.withdraw_amount = withdraw_amount
        # print(self.balance)
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f"Your current balance is {self.balance}")

        else:
            print(f"The withdrawal amount of {withdraw_amount} is exceeding your available balance!")
        # return self.balance


# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print(acct1)

# # 3. Show the account owner attribute
acct1.owner

# # 4. Show the account balance attribute
acct1.balance

# # 5. Make a series of deposits and withdrawals
acct1.deposit(50)
# acct1.deposit(50)
# acct1.deposit(50)
# acct1.deposit(50)

# acct1.withdraw(75)


# # 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(20)


# # ## Good job!
