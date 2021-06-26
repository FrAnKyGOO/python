#สี่เหลี่ยมจตุรัส

number = int(input("number = "))

for row in range(1,number+1):
    for column in range(1,number+1):
        print(column,end='')
    print(" ")




for row in range(number):
    for column in range(number):
        print("x",end='')
    print(" ")