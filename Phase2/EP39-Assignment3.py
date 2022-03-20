# Assignment หากลุ่มเลขคู่ /เลขคี่
number=[]
odd=[] # เลขคู่
even=[] # เลขคี่
while True:
    x=int(input('ป้อนค่าตัวเลข'))
    if x<0: 
        break
    if x%2 ==0 :
        even.append(x)
    else:
        odd.append(x)

print('เลขคู่ ',even)
print('เลขคี่ ',odd)
    
