data=input("Enter a data: ")
reverse =""
for ch in data:
    reverse = ch + reverse

if data == reverse :
    print("Palindrome")
else:
    print("not Palindrome")        




