'''การนิยาม , constructor
การเข้าถึงข้อมูล
การเข้าถึงข้อมูลแบบกำหนดช่วง (Sli
การแก้ไขข้อมูล
แสดงผลด้วย Loop
ตรวจสอบข้อมูล
นับจำนวนสมาชิก (len)
len() ทำงานร่วมกับ Loop For
A1sLWuziaya => append, inser
การลบข้อมูล => remove , pop ,del ,clear
การคัดลอกข้อมูล
การรวมข้อมูล (+)
แสดงจำนวนสมาชิก (Count)'''

# non primitve : list

number=[] # list u
number=[1,2,3,4,5,6] # list
name=["unu N","unu B","unu o"]
all=[10,"unolzi", True, 3.14,-1]
#แสดงผล
# print(name)
# print(all)
# print(number)
fruit=["มะม่วง","มะนาว", "มะยม"]
name1=["מ" ,"ה" ]

for i in range(len(fruit)):
    print(i)

print("ก่อรเพิ่ม=>",fruit)
fruit.append("มะขิวด")
print("หลังเพิ่ม=>",fruit)

#insert (index, NUninluu)
print("หลังเพิ่ม=>",fruit)
fruit.insert(1,"nitu")
print("หลังแทรก=>",fruit)

fruit.remove("มะยม")
print("Remove =>",fruit)     
fruit.pop()
print("pop =>",fruit)     

del fruit[1]
print("del =>",fruit)     
'''del fruit ลบทิ้เลยทั้งตัวแปล
print("del =>",fruit)   
fruit.clear()
print(fruit)
'''  
x=[]
print(x)
x=fruit.copy()
print(x)

number=[1,2,3,4,5,6,7,8,9,10] # list üau
fruit=["มะม่วง","มะนาว", "มะยม","มะละกอ"]
allGroup=number+fruit
print(allGroup)

number=[1,2,3,4,5,6,7,8,9,10,5,6,5,3,5,5]
x=number.count(5) #integer
print(x)

number.extend(fruit)

print(number)