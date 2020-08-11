
from Bank_class import Bank 
b1 = Bank("1",0,100,"PAN1")
a = b1.deposit(1000) 
print("account 1:",a)

b2 = Bank("2",1000,100,"PAN2")

print("account 2:",b2.deposit(1000))

b3 = Bank("3",5000,100,"PAN3")

print("account 3:",b3.withdraw(1000))

