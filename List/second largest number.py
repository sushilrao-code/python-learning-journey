num=[10,50,30,80,20]
largest=num[0]
for i in num:
    if i>largest:
        largest=i
second_largest=None     

for i in num:
    if i!=largest:
        if second_largest is None or i>second_largest:
            second_largest=i
print("largest number is",largest)
print("second largest number is",second_largest)