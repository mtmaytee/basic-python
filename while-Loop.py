# โครงส้รางควบคุมแบบทำซ้ำ
'''
i=1
while i<3:
    print("hello World")
    i += 1

for l in range(1,6,2): #range start 0 range(start,stop,step)
    print("รอบที่ = ",l)
'''
'''o = 0
while o<20:  
    o+=1
    space = 20-o
    for s in range(space):
        print(" ", end='')
    for n in range(1,(20 - space)+1):
        print('*',end='')
    for n in reversed(range(1,o)):
        print('*',end='')

    print("")
'''

# break หยุด / continue กระโดดการทำงาน
'''
i=1
while i<=10:
    print("รอบที่ = ",i)
    if i==5:
        print("จบ")
        break
    i+=1
i=1
while i<=10:
    print("รอยที่ ",i)
    i+=1
else:
    print("จบ")


i=0
while i<=10:
    i+=1    
    if (i%2 !=0):
        continue
    print("รอยที่ ",i)
    
else:
    print("จบ")

for i in range(1,11):
    if (i%2 ==0):
        continue
    print("รอยที่ ",i)
    '''