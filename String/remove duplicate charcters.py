name = "silent"
freq = {}
result =" "
for ch in name:
    if ch not in freq:
        freq[ch]=1
        result +=ch 

print(result)

