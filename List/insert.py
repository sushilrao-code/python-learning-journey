num=[1,3,4,5,6,7]
mid=len(num)//2
new_list=[]
new_list1=[]
for i in range(len(num)):
    if i==mid:
        new_list.append(999)
    new_list.append(num[i])
    
for i in new_list:   
    new_list1.append(i)
new_list1.append(999)    

print(new_list1)