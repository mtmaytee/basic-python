# Assignment รับและเรียงลำดับ

number =[]
while True:
    x= int(input("ป้อนข้อมูล "))
    if x<0:
        break
    number.append(x) 
print("ก่อนเรียง=>",number)
number.sort()
print("น้อยไปมาก=>",number)
number.reverse()
print("มากไปน้อย=>",number)
print('จบโปรแกรม')