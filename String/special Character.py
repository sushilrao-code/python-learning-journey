number = "abc122#@"
count =0
special="@#$%^&*()_+=-,<.>/?;:|"
for num in number:
    if  num in special:
        count +=1
        
print(count)        
