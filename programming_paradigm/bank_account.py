class BankAccount:
    def __init__(self,bal =0):
        self.account_balance = bal
    
    def deposit(self, amount):
        self.account_balance += amount

    def  withdraw(self,amount):
        fundSufficient =  self.account_balance >= amount
        if fundSufficient:
            self.account_balance -= amount
            return fundSufficient
        else:
            return fundSufficient
    def display_balance(self):
        print('Current Balance: ${}.00' . format(self.account_balance))

