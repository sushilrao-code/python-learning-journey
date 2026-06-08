a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
x=a
y=b
while y>0:
    temp =y
    y=x%y
    x=temp
    
print("GCD =", x)
gcd=x
print("LCM =", (a * b) // gcd)