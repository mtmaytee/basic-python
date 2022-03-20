# Set คือ ชนิดข้อมูล คุณสมบัติ ไม่สามารถซ้ำกันได้ ไม่เหมือน list tuple
"""จัดกลุ่มข้อมูลพื้นฐาน
List    = [] , ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันได้, ซ้ายไปขวา
Tuple   = () ,ข้อมูลต่างชนิดกัน , แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันได้, ซ้ายไปขวา   
Set     = {} , ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันไม่ได้, ล่าดับไม่แน่นอน 
"""

fruit = {"มะม่วง","มะขาม","มะยม",50,True}
fruit.add("ทุเรียน")
lis  = ["ชะอม","สัปปะรด"]
#เพิ่มสมาชิกหลายตัว
fruit.update(lis)
#constructor
fish=set (["ปลาดุก" , "ปลาหมอ" , "ปลาดุก"])
print(fruit)

for item in fruit:
    print('data => ',item)

if 'ปลาดุก' in fruit:
    print('มี')
else:
    print('ไม่มี')

# ลบข้อมูล

#fruit.remove('ปลาดุก')
# ลบแต่ไม่แสดง error 
fruit.discard('มะยม')
# ล้างค่า
fruit.clear()
# ลบตัวแปลทิ้ง
del fruit

#union เอามารวมกัน 
'''fruitA={"กล้วย", "มะยม", "มะนาว"}
fruitB={"สตอว์เบอรรี่" , "กีวี" , "มะม่วง"}
allFruit=fruitA.union(fruitB) 
# หรือ 
fruitA.update(fruitB)
print(fruitA)

# copy set 

fruitC = fruitA.copy()
print(fruitC)
'''
#difference แยกสมาชิกข้อมูลของ fruitA ต่างจาก fruitB อย่างไร  ทำการสร้าง fruitC โดยทำการลบข้อมูลของ fruitB ตัวที่มีใน fruitA ออกไป แล้วเอาตัวที่เหลือของ fruitA มากเก็บลง fruitC
#intersection รวมสมาชิกของ fruitAและfruitB แล้วเอาตัวที่เหมือนกัน fruitAและfruitB มากเก็บลง fruitD

fruitA={"กล้วย", "มะยม" , "มะนาว", "แอปเปิ้ล" , "ทุเรียน" }
fruitB={"แอปเปิ้ล","ทุเรียน" , "สตอว์เบอรรี่" , "กีวี" , "มะม่วง"}

fruitC = fruitA.difference(fruitB)

fruitD = fruitA.intersection(fruitB)

print(fruitC)
print(fruitD)
fruitA.intersection_update(fruitB)
#fruitA.difference_update(fruitB)
print(fruitA)

#subset
fish={"ปลาดุก", "ปลาหมอ" , "ปลาวาฬ","ปลาโลมา", "ปลาฉลาม" , "ปลาตะเพียน"}




