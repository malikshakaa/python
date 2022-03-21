class User:	
    def __init__(self, name, email,bankacount):
        self.name = name
        self.email = email
        self.bankacount = bankacount


    def make_deposit(self, amount):
        self.bankacount.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.bankacount.withdraw(amount)
        return self

    def display_user_balance(self):
        self.bankacount.display_account_info()
        return self
    
    def transfer_money(self,user2,amount1):
        self.bankacount.withdraw(amount1)
        user2.bankacount.deposit(amount1)
        return self

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

acount1=BankAccoun(0.02,200)
acount2=BankAccoun(0.03,300)
majed=User("malik", "malik@hotmail.com",acount2)
malik=User("malik", "malik@hotmail.com",acount1)
malik.make_deposit(200).make_withdrawal(100).transfer_money(majed,50).display_user_balance()
