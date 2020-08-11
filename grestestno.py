##Take 3 values from user and find the grestest number

x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
z = int(input("Enter the third number"))

if (x > y) and (x > z):
    print(x)

elif (y > z) and (y > x):
    print(y)

elif (z > x) and (z > y):
    print(z)        

else:
    print("Invalid Number")    