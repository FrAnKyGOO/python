def convert():
    number = input("temperature = ")

    a = int(number[:-1]) #เก็บตัวเลขทั้งหมดก่อนตัวสุดท้าย
    b = number[-1].upper() #เก็บอักษรสุดท้าย

    if b == "C":
        ans = (a*9)/5+32
        c = "F"
    if b == "F":
        ans = (a-32)*5/9
        c = "C"
    print("temperature = ","%.2f" % ans,c)    
convert()        
