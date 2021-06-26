name = " kittisak "
name_1 = "KITTISAK"
name_2 = "Kittisak frank"
name_3 = "kittisak nuntasen frankygo"
name_4 = "NUNTASEN"

print(len(name))# หาความยาวของข้อความ

name.split #ลบช่องวางในข้อความ

name.lstrip  #ลบช่องวางซ้าย rsptrip ลบขวา

print(name)

print(name_1.lower()) #พิมเล็ก

print(name.upper()) #พิมใหญ่

print(name.capitalize()) #ขึ้นต้นเป็นพิมใหญ่

print(name_2.replace("frank","Nuntasen")) #แทนที่ตัวหน้าโดยจัวหลัง

x = "frankygo" in name_3 #เช็คข้อความว่ามีอยู่ไหม
print(x)

print(name_1 +" "+ name_4) #ต่อ string
text = "ชื่อ :{}\tนามสกุล :{}"
print(text.format(name_1,name_4))

a = "1 2 2 3 3 4 4 5 5 2 2 3 4"
print(a.count("2")) #หาตำแหน่งว่ามีกี่ที่



