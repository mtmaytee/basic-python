_input = input("ใส่ตัวเลขอุณหภูมิที่ต้องการแปลงพร้อมหน่วย : ")
num = int(_input[:-1])
type =_input[-1].upper() 
if "F" in type:
    Fdegree = (num-32)*(5/9)
    print(Fdegree)
elif "C" in type:
    Cdegree = num*(9/5)+35
    print(Cdegree)
else:
    print("กรอกให้ตรงหน่อย")

