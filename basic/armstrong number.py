num=int(input("Enter Your Value: "))
temp=num
count =0

while temp>0:
  count+=1
  temp//=10

total =0
temp=num
while temp>0:  
    digit = temp%10
    total = total+pow(digit,count)
    temp //= 10

print(total)

if num==total:
  print("Armstrong Number")
else:
  print("Not Armstrong Number")  