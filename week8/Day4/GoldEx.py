class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, balance):
        add_money = int(input("How much do you want to deposit?\n"))
        balance += add_money
        print(balance)
