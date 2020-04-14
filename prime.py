
num=4

for i in range(2,int(pow(num,0.5))):
    if num%i ==0:
       print("Not prime")
       break
else:
   print("Prime")