#Create a class BankAccount with deposit and withdraw methods. Use encapsulation to protect balance.

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(5000)
acc.withdraw(1000)
print(acc.get_balance())
