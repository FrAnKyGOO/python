def Bmi():
    kg  = int(input("น้ำหนัก = "))
    wh = int(input("ส่วนสูง = "))
    wh = wh / 100
    bmi = kg / wh**2
    print("BMI = ","%.2f" % bmi)
    if bmi<=18.0:
        print("ต่ำ")
    elif bmi>=18.5 and bmi<=22.9:
        print("สมส่วน")   
    return 0
Bmi()    