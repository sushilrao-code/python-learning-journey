num = [1, 2, 2, 3, 3, 4, 4,6,7,6,7,8,9,89,9,8, 5]
unique = []
for i in num:
    if i not in unique:
        unique.append(i)
        # print(unique)
    elif i in unique:
        print(i)  