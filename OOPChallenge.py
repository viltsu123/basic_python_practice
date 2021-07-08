class Account:

    def __init__(self, owner, initBalance):
        self.owner = owner
        self.totalBalance = initBalance

    def deposit(self, deposit):
        self.totalBalance += deposit
        return "deposit made, new balance = {}".format(self.totalBalance)

    def withdraw(self, withdraw):
        if self.totalBalance - withdraw < 0:
            return f"insufficient funds, balance = {self.totalBalance}"
        else:
            self.totalBalance -= withdraw
            return f"withdraw made, new balance = ${self.totalBalance}\nAccount owner:   {self.owner}"

    def accountInfo(self):
        return self.totalBalance, self.owner

account = Account("Vilitsu", 5000)
print(account.accountInfo())
print(account.deposit(50))
print(account.withdraw(6000))
print(account.withdraw(500))
print(account.owner)
print(account.totalBalance)
