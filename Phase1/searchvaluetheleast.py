max,min = 0,0

while True:
    num = int(input("ป้อนตัวเลขของคุณ "))

    if num <0:
        print("ไม่รับค่าติดลบ")
        break

    if num>max:
        max=num

    print("ค่ามากสุด",max,"ค่าน้อยสุด",min)   