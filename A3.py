#ตารางมากฮ็อด

number = int(input("number = "))

for row in range(number):
    for column in range(number):
        if (row + column)%2 == 0:
            print("x",end='')
        else:
            print("o",end='')    
    print(" ")    



#ขอบสี่เหลี่ยม

number1 = int(input("number = "))

for row in range(number1):
    for column in range(number1):
        if row == 0 or row==number1 or column==number-1:
            print("x",end='')
        else:
            print(" ",end='')
    print(" ")    

