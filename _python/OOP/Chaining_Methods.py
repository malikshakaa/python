class User:	
    def __init__(self, name, email):
        self.name = "malik"
        self.email = "malik.a.shakaa@gmail.com"
        self.account_balance = 0


    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self
    
    def transfer_money(self,user2,amount1):
        self.make_withdrawal(amount1)
        user2.make_deposit(amount1)
        return self

malik = User("malik","malikemail@gmail.com")
majed = User("malik","malikemail@gmail.com")
raed = User("malik","malikemail@gmail.com")

malik.make_deposit(300).make_deposit(400).make_deposit(200).make_withdrawal(500).display_user_balance()
majed.make_deposit(100).make_deposit(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()
raed.make_deposit(300).make_withdrawal(200).make_withdrawal(50).make_withdrawal(50).display_user_balance()
malik.transfer_money(majed,100).display_user_balance()
majed.display_user_balance()
