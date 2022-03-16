

start , stop = 1,5
sum,avg=0,0
while(start<=stop):
    num = int(input("รับค่าตัวเลข"))
    sum+=num
    start+=1
avg=sum/stop
print(avg)

print(sum)
