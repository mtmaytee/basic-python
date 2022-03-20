# เกมทายเลชลูกเต๋า

import random


k=0
while True:
    num = int(input('กรอกเลข : '))
    if num<=0 or k==3:
        break
    correct = (num==random.randrange(1,10))

    if correct :
        print("ตอบถูก")
        break

    else:
        print('ไม่ถูก',k)
        
    k+=1