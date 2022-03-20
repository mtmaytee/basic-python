# list , tuple
lis=["สีแดง", "สีเหลือง" , "สีเขียว"]
tup=("สีแดง", "สีเหลือง" , "สีเขียว")
#dictionary => key (การเข้าถึงข้อมูล) , value (ค่าของข้อมูล)
#การสร้าง dict
# iaduls = {key:value, key:value, key:value}
colors={"red": "สีแดง" , "yellow" :"สีเหลือง" , "green":"สีเขียว" ,98:"บ้านแสนสุข" , 100:"บ้านป่า",True:"marry",False:"sign"}
kity={"bangkok":"กรุงเทพ"}
animal={"ไก่":"chicken", "แมว":"cat","หมา":"dog"}
student={"ต้น":40, "ธี":50, "นาย":100}
room={300:"นาย A",301:"นาย B",302: "นาย C"}

#constructor
pets=dict(cat="แมว", dog="หมา", duck="เป็ด")

print(colors["red"])
print(colors[100])
print(colors.get("red"))
print(colors[True])

# การแก้ไขข้อมูล
colors[100]="บ้านสวน"
print(colors[100])

# เพิ่มข้อมูล update มีความสามารถ 2 อย่างคือ ถ้า key ไม่ซ้ำก็เพิ่มข้อมูลลงไป แต่ถ้าซ้ำก็ทำการแก้ไขข้อมูลที่ key นั้น 

colors.update({"blue":"สีน้ำเงิน","orange":"สีส้ม","red":"สีชมพู"})
print(colors)


                 