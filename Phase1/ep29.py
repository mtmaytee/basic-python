

'''start , stop = 1,5
sum,avg=0,0
while(start<=stop):
    num = int(input("รับค่าตัวเลข"))
    sum+=num
    start+=1
avg=sum/stop
print(avg)

print(sum)'''

sum = 0

'''while sum<100:
    number = int(input("input number"))
    sum+=number
    print("ผลรวม = ",sum)
'''
while True:
    number = int(input("input number "))
    sum+=number
    if sum>=100:
        break
    print("ผลรวม = ",sum)