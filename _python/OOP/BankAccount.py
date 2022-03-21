class BankAccoun:
    def __init__(self, int_rate=0, balance=0):
        self.balance=balance
        self.rate=int_rate
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee" and deduct $5')
        else:
            self.balance-=amount
        return self

    def display_account_info(self):
            print("Balance:",self.balance)
            return self
    def yield_interest(self):
        self.balance=self.balance+self.balance*self.rate
        return self


acount1 = BankAccoun (0.06,100 )
acount2 = BankAccoun (0.05,300)

acount1.deposit(200).deposit(100).deposit(50).withdraw(100).yield_interest().display_account_info()
acount2.deposit(200).deposit(100).withdraw(50).withdraw(100).withdraw(100).withdraw(600).yield_interest().display_account_info()


