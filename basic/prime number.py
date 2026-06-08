num=int(input("Enter Your Value: "))
for i in range (2,int(num**0.5)+1):
    if num%i==0:
        print("Not Prime")
        break
else:
    if num>1:
     print("Prime") 
    else:
      print('Not Prime')        