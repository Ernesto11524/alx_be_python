class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance = amount + self.account_balance
        
    def withdraw(self, amount):
        if self.account_balance >= amount:
            print(f"Withdrawing...... ${amount:.1f}")
            current_balance = self.account_balance - amount
            self.account_balance = current_balance
            return self.account_balance
        else:
            print("Insufficient funds. You cannot withdraw more than your current balance.")
            self.display_balance()
            return self.account_balance
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")       