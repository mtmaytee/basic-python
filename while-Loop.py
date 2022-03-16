# โครงส้รางควบคุมแบบทำซ้ำ

i=1
while i<3:
    print("hello World")
    i += 1

for l in range(1,6,2): #range start 0 range(start,stop,step)
    print("รอบที่ = ",l)

o = 1
text ="*"
while o<100:
    
    print(text[-o:])
    text +=text
    o+=1
