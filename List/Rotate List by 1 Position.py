num=[1,2,3,4,5]
# last= num[-1]
# num.pop()
# num.insert(0,last)
num=[num[-1]]+ num[:-1]
print(num)