num = int(input("Enter a number: "))
count =0
total=0
for i in range(1, num + 1):
    if num % i == 0:
        total += i
        count += 1

print("Factors = ", count)
print("Sum of factors = ", total)
