class WithdrawException(Exception):
    pass


class BankAccount:
    def __init__(self,initial_amt:float,acc_name:str):
        self.balance = initial_amt
        self.acc_name = acc_name
        print(f"\n Account '{self.acc_name}' Created.\n Balance:${self.balance:.2f}")

    @property
    def getBalance(self):
        print(f"Account: '{self.acc_name}' Current Balance: ${self.balance}")

    def __str__(self):
        return f"\n**Account Name: {self.acc_name},\nCurrent Balance: ${self.balance}\nAccount Type: General Account**\n"

    def deposit(self,amt:float):
        self.balance += amt
        print(f"\nDeposit Completed.")
        self.getBalance

    def balance_check(self,amt):
        if self.balance >= amt:
            return
        else:
            raise WithdrawException(f"Sorry, Account '{self.acc_name}' Has Only balance ${self.balance:.2f}")

    def withdraw(self,amt):
       try:
           self.balance_check(amt)
           self.balance -= amt
           print("Withdrawn Completed")
           self.getBalance

       except WithdrawException as e:
           print(f"\nWithdraw Interrupted!!\n{e}")

    def transfer(self, amt, acc_name):
        try:
            print("\n\n***************************")
            print("Transfer Beginning....🚀")
            self.balance_check(amt)
            self.withdraw(amt)
            acc_name.deposit(amt)
            print("Transfer Complete.👍")
            print("\n\nThanks for staying with us")
            print("****************************\n")
        except WithdrawException as e:
            print(f"\nTranster Interrupt!! {e}")

class InterestRewardsAccount(BankAccount):
    def deposit(self, amt):
        return super().deposit(amt*1.05)

    def __str__(self):
        return f"\n**Account Name: {self.acc_name},\nCurrent Balance: ${self.balance}\nAccount Type: Interest Rewards Account**\n"


class SavingsAccount(InterestRewardsAccount):
    withdraw_fee = 5
    def __init__(self, initial_amt: float, acc_name: str):
        super().__init__(initial_amt, acc_name)

    def __str__(self):
        return f"\n**Account Name: {self.acc_name},\nCurrent Balance: ${self.balance}\nAccount Type: Savings Account**\n"


    def withdraw(self, amt):
        return super().withdraw(amt+self.withdraw_fee)