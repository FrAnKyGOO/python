def exchange():
    money = int(input("number is money = "))
    if money/1000!=0:
        amount = money//1000
        money = money%1000
        print("1000 = ",amount,"ใบ")
    if money/500!=0:
        amount = money//500
        money = money%500
        print("500 = ",amount,"ใบ")
    if money/100!=0:
        amount = money//100
        money = money%100
        print("100 = ",amount,"ใบ")
    if money/50!=0:
        amount = money//50
        money = money%50
        print("50 = ",amount,"ใบ")  
    if money/20!=0:
        amount = money//20
        money = money%20
        print("20 = ",amount,"ใบ")
    if money/10!=0:
        amount = money//10
        money = money%10
        print("10 = ",amount,"เหรียญ")
    if money/5!=0:
        amount = money//5
        money = money%5
        print("5 = ",amount,"เหรียญ")        
    if money/1!=0:
        amount = money//1
        money = money%1
        print("1 = ",amount,"เหรียญ")
exchange()        