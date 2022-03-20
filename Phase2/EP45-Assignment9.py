#การค้นหาและนับจำนวนตัวอักษรในสมาชิก
message=["aa","aab","cba","bba","aba","cca"]
result=[]

for itme in message:
     
     result.append(itme.count("a"))
print(result)