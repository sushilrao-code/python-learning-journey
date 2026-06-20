num=[1,0,3,0,-4,-75,0]
result=[]
positive=[]
for i in range(len(num)):
    if num[i]<0:
       result.append(num[i])
    else:
       positive.append(num[i])
    
print( result +positive)