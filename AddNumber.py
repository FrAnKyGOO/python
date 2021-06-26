start = int(input("start number = ")) 
stop = int(input("stop number = ")) 
sum = 0

while (start <= stop):
    number = int(input("number = "))
    start +=1
    sum += number

print("total =", sum)    



sum = 0

while True:
    number = int(input("number = "))
    sum += number
    if sum<=100:
        break
    print("ผลรวม = ", sum)