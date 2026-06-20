num=[3,57,8,4,5]
for i in range(1,4):
    largest=max(num)
    print(f"{i} Largest: {largest}")
    num.remove(largest)