# tuple กับ list เหมือนกัน แต่ tuple เปลี่ยนแปลงข้อมูลไมไ่ด้ 
'''การนิยาม , constructor
การเข้าถึงข้อมูล
การเข้าถึงข้อมูลแบบกำหนดช่วง (Slice)
การแก้ไขข้อมูล
แสดงผลด้วย Loop
ตรวจสอบข้อมูล
นับจำนวนสมาชิก (len)
len() ทำงานร่วมกับ Loop For
การสร้างและเพิ่มข้อมูล (Join)
ทำงานร่วมกับ List
การลบข้อมูล del , การลบแบบ list
ค้นหาและนับจำนวนสมาชิก (Count)
ค้นหาสมาชิกด้วย Index
การ Sort ข้อมูล
'''
#constructor tup= tuple(())
from ntpath import join
from operator import index


tup=tuple((1,2,3,4,"kongruksiam","มะม่วง",True, 3.99)) # tuple
lis=list(tup)#list
lis[0]="กรุงเทพ"
print(tup)
tup=tuple(lis)
print(tup)
print(lis)

for i in tup:
    print(i)

if "มะม่วง" in tup:
    print("เป็นสมาชิก")
else :
   print ("ไม่เป็นสมาชิก")
#range 0-7 
for item in range (len(tup)):
    print(tup[item]) # tup[0] , tup[1] ,....tup[7]] %23

name=("kongruksiam","jojo")
new="nut" # new=("nut",)
#name=name+(new,)
allgroup = name+(new,)

city=["กรุงเทพ",  "ชลบุรี" , "อุบล"] 
tup=tup+tuple(city)
print(tup)

#del city

print(tup)
print("Before =>",tup)
lis=list(tup)
lis.pop()
tup=tuple(lis)
print(tup)

x=tup.count(4) #นับจำนวน
print(x)
x=tup.index(4) #ตำแหน่ง 
print(x)

# sort การเลียงข้อมูลจ้องยืมความสามารถของ list 
tup=(100,99,88,50,200,1,2,3,4,3.99,4) # tuple
print("Brfor",tup)
lis=list(tup)
lis.sort()
tup=tuple(lis)
print("After",tup)

# นำค่าใน tuple => ตัวแปร
tup=(10,20,30)
a,b,c=tup
a,b=b,a #สลับ ค่า
print(a,b,c)

#  สลับค่าtuple x,y=y,x
x=(50,60)
y=(88,99)

x,y=y,x

# tuple => string รวมตัวอักษร ด้วยคำสั่ง join
character =('k','o','n','g')
name="".join(character)
print(name)

# reversed string to tuple
x="kongruksiam"
y=tuple(reversed(x))
name="".join(y)

print(name)
