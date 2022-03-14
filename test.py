
w = int(input("กรอกน้ำหกนัก kg :"))
h = (int(input("กรอกส่วนสูง cm :"))/100)**2

total = w/h
if total>30:
    text = "อ้วนมาก / โรคอ้วนระดับ 3"
elif total>=25 and total<=29.90:
    text = "อ้วน / โรคอ้วนระดับ 2"
elif total>=23 and total<=24.90:
    text = "ท้วม / โรคอ้วนระดับ 1"
elif total>18.50 and total<=22.90:
    text = "ปกติ (สุขภาพดี)"
else:
    text = "น้ำหนักน้อย / ผอม"    

print(text," ค่าbmi ",'%.2f' %(total))

