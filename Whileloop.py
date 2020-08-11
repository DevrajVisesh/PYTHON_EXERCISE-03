##While Loop Exercises

#i = 5 

#while i >= 1:
#    print("oyy", i)
#    i = i - 1

#----------------------------------------

# i = 1

#while i <= 5:
#    print("hey",end="")
#    j = 1
        
#    while j <= 3:
#            print("Yoo",end="")
#            j = j + 1

#    i = i + 1
#    print()

#----------------------------------------

#i = 1

#while i <= 4:
#    print("#",end="")
#    j = 1

#    while j <= 4:
#        print("#",end="")
#        j = j + 1

#    i = i + 1
#    print()

#----------------------------------------

#Write a code to print the valuse from 1 to 100 
#and skip the number which are divisible by 3 or 5.

i=1

while i<=100:
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    i=i+1 
print()