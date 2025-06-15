class BankAccount:
    def __init__(self,Balance = 0):
        self.Balance = Balance
    
    def deposit(self,amount):
        self.Balance += amount
    
    def withdraw(self,amount):
        if (self.Balance - amount) >= 0:
            self.Balance -= amount
            return True
        
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.Balance:.2f}")
