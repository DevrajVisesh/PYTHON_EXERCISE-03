#print(r'visesh \n devraj')

#name = "visesh"
#print(name = [-3])

#x = ['Visesh,5.6,19']

#print(x)

#i=1
#while 1<=100:
#    print(i,end="")
#    i=i+1 
#print()

import math

# Taking the input from user
number = int(input("Enter the Number"))

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")