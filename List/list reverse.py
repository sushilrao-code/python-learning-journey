num=[10,50,30,80,20]
print(num[::-1])#using slicing
result=[]
for i in range(len(num)-1,-1,-1):#using for loop
    result.append(num[i])
print(result)
num.reverse()#using reverse method
print(num)