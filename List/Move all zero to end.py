num=[1,0,3,0,4,5,0]
result=[]
zero=[]
for i in range(len(num)):
    if num[i]==0:
       zero.append(0)
    else:
        result.append(num[i])
    
print(result + zero)