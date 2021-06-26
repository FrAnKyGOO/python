#เกมท้ายลูกเต๋า

import random

my_random = random.randrange(1,7)
k = 1
correct = False

print(my_random)

while True:
    number = int(input("your number = "))
    if number<0 or k == 3:
        break
    correct = (number==my_random)
    if not correct:
        if(number>my_random):
            print("<")
        else:
            print(">")     
    if correct:
        print("True")
        break
    else:
        print("False")    
    k+=1 

if not correct:
    print("Sorry!!")
    print("random = ",my_random)    
