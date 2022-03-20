# Assignment รับและเรียงลำดับ หาค่ามากที่สุด น้อยสุด
# ใช้ function min max avg
from audioop import avg


number =[]
while True:
    x= int(input("ป้อนข้อมูล "))
    if x<0:
        break
    number.append(x) 

print('ค่าที่มากที่สุด ',max(number))
print('ค่าที่น้อยที่สุด ',min(number))
print('ผลรวม ',sum(number))
print('ข้อมูลทั้งหมด ',number)
