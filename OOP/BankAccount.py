class BankAccount:
    def __init__ (self, balance : int, account_num : int):
        self.__balance = balance
        self.account_num = account_num
        
    
    def deposit(self, account_num, amount):
        if self.account_num == account_num:
            self.__balance = amount + self.__balance
            return self.__balance
        else :
            return " Account num not found "
    
    def withdraw(self, account_num, amount):
        if self.account_num == account_num:
            if self.__balance > amount: 
                self.__balance = self.__balance - amount 
                return self.__balance
            else:
                return "balance is not sufficient "
        else :
            return "account not found"

    def check_balance(self, account_num):
        if self.account_num == account_num:
            return self.__balance

b = BankAccount(1000,1234)
print("Current balance ",b.check_balance(1234))
print("Deposit amount ",b.deposit(1234,100))
print("Withdraw amount ",b.withdraw(1234,300))
print("Current balance ",b.check_balance(1234))
