from turtle import st


steps = int(input("ตัวเลขที่ต้องการ : "))

for i in range(1,steps+1):
    for n in range(1,i+1):
        print('*',end='')
    print("")