from BankAccount import *

Mirza = BankAccount(1000,"Mirza Abbas")
Sanjana = BankAccount(2000,"Sanjana Hossain")

Mirza.getBalance
Mirza.deposit(500)

Sanjana.withdraw(20000)

Mirza.transfer(3000, Sanjana)
Mirza.transfer(300, Sanjana)

Jim = InterestRewardsAccount(2000, "Jim")
Jim.deposit(100)
Jim.transfer(100, Sanjana)


Doe = SavingsAccount(1000,"Doe")
Doe.deposit(200)
Doe.withdraw(200)
Doe.transfer(100,Mirza)

print(Mirza)
print(Jim)
print(Doe)