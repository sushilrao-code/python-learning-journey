num = [10, 29, 30, 40, 90]
search=int(input("Enter your Number: "))
pos=1
found=False

# for n in num:
#     if n==search:
#         print("Found at position:",pos)
#         found=True
#     pos=pos+1

# if not found:
#     print("Number not found!")      

for n in range(len(num)):
    if num[n]  ==search:
        print("Found at position:",n)
        found=True
if not found:
    print("Number not found!")          