#A program to print all the perfect square numbers between 1 to 50

i=1

for i in range(1,50):

    if i**2<=50:
        print(i,"=",i**2)
    elif i**2>50:
        break
       
    

