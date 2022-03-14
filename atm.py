inputmoney = int(input("กรอกเงินตรงนี้ : "))
'''
bank100,bank500,bank1000  = 1000,120,100

def Bank1000(inputmoney):
    outputmoney1000 = inputmoney//1000 #จำนวนเงินที่จ่ายเป็นแบงพัน
    #sumbank1000 = bank1000-outputmoney1000 #จำนวนแบงที่มีอยู่จ่ายได้โดยลบกับจำนวนเงินที่ต้องการ
    inputmoney %= 1000 #เงินส่วนที่เหลือที่ไม่ใช้แบงพัน
    text = " จำนวนแบงค์พัน "+str(outputmoney1000)

    if inputmoney!=0:
        if inputmoney>=500:
            data = Bank500(inputmoney)
            inputmoney = data[1]
            if inputmoney!=0:
                data = Bank100(inputmoney)
                text += data[0]
                inputmoney = data[1]
                if inputmoney!=0:
                    dataArray = "error"
                else:
                    text += data[0]
                    dataArray = text 
            else:
                text += data[0]
                dataArray = text  

        elif inputmoney>=100: 
            data = Bank100(inputmoney)
            inputmoney = data[1]
            if inputmoney!=0:
                dataArray = "error"
            else:
                text += data[0]
                dataArray = text 
    else:    
        dataArray = text
    
    return dataArray


    

def Bank500(inputmoney):
    outputmoney500 = inputmoney//500 #จำนวนเงินที่จ่ายเป็นแบง500
    #sumbank500 = bank500-outputmoney500 #จำนวนแบงที่มีอยู่จ่ายได้โดยลบกับจำนวนเงินที่ต้องการ
    inputmoney %= 500 #เงินส่วนที่เหลือที่ไม่ใช้แบง500
    text = " จำนวนแบงค์ห้าร้อย "+str(outputmoney500)
    dataArray = [text,inputmoney]
    return dataArray

def Bank100(inputmoney):
    outputmoney100 = inputmoney//100 #จำนวนเงินที่จ่ายเป็นแบง100
    #sumbank500 = bank500-outputmoney100 #จำนวนแบงที่มีอยู่จ่ายได้โดยลบกับจำนวนเงินที่ต้องการ
    inputmoney %= 100 #เงินส่วนที่เหลือที่ไม่ใช้แบง100
    text = " จำนวนแบงค์หนึ่งร้อย "+str(outputmoney100)
    dataArray = [text,inputmoney]
    return dataArray
'''

if inputmoney>=1000:
    outputmoney1000 = inputmoney//1000
    inputmoney %= 1000
if inputmoney>=500:
    outputmoney5000 = inputmoney//500
    inputmoney %= 500
if inputmoney>=100:
    outputmoney100 = inputmoney//100
    inputmoney %= 100