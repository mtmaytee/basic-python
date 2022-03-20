from fnmatch import fnmatchcase


name = " maytee khankaew อายุ 26 สูง 126 "
# คำสั่งที่ใข้กับ str เช่นลบค่าว่าง เปลี่ยนพิมเล็กพิมใหญ่ 
print(name[0:3]) # เริ่มต้นที่ 0 จะถึงก่อน ตำแหนางที่3 
print(name[:3]) # แบบนี้คือ ไม่เขียนเลข0 ก็ได้
print(name[-3])
print(name[-2:])

# len function หาความยาว นับค่าว่างด้วย
print(name)
print(len(name))

# strip function ลบช่องว่าซ้ายขาวได้
#name=name.strip()
name=name.lstrip() #ลบช่ิองว่างด้านซ้าน
#name=name.rstrip() #ลบช่ิองว่างด้านซ้าน

print("strip ",name)
print("len ",len(name))

# upper function ทำให้เป็นตัวพิมใหญ่ 
print("upper ",name.upper())

# lower function ทำให้เป็นตัวพิมเล็ก
print("lower ",name.lower())

# capitalize function ทำให้ตัวแรกสุดเป็นตัวพิมใหญ่
print("capitalize ",name.capitalize())

# replace function ทำให้แทนที่ฉะเพาะจุด replace("หา","เปลี่ยน","ตำแหน่งที่เจอ")
print("replace ",name.replace("26","15",1))

# in function ทำให้เช็คข้อความ ให้ค่า true false
_search = "อายุ" in name
print("in ",_search)

# การต่อ Stringหรือเรียกว่า concatinate +

fname = "maytee"
lname = "khankaew"
age = "26"
fullname = fname+lname+age
ry = 19568.58678

# การจัดรูปแบบการแสดงผล {}
text = "ชื่อต้น :{0}\tนามสกุล :{1}\tอายุ :{2}\tอาชีพ :{3}\tเงินเดือน:{4:.2f}"
print(text.format(fname,lname,age,"programmer",ry))

#  นับจำนวนคำในประโยค
fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด"
print(fruit.count("ทุเรียน"))

# เช็คคำขึ้นต้น startswith และลงท้าย endswith

Name="นางนิภา พรใจดี"
#Name.endswith("")
print(Name.startswith("นาย"))

if Name.startswith("นาย"):
    Name += "\tเพศชาย"
else:
    Name += "\tเพศหญิง"

print(Name)
