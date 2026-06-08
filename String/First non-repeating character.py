name = "abcreaa"
freq = {}
for ch in name:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for ch in name:
    if freq[ch]==1:
        print(ch)
        break
    else:
        print("Non -repeating charcter")    
