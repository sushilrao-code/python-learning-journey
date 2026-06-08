name = "abcreaa"
freq = {}
for ch in name:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

print(freq)
