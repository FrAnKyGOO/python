max , min = 0,0

while True:
    number = int(input("number = "))
    if number <=0:
        break
    if number > max:
        max=number
    if number < min:
        min = number


print("End Program")
print("max = ", max)
print("min = ", min)            