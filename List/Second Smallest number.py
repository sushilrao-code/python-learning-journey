num=[10,50,30,80,20]
smallest=num[0]
for i in num:
    if i<smallest:
        smallest=i
second_smallest=None     

for i in num:
    if i!=smallest:
        if second_smallest is None or i<second_smallest:
            second_smallest=i
print("smallest number is",smallest)
print("second smallest number is",second_smallest)