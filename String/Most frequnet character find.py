name = "abcreaa"
freq = {}
for ch in name:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

max_count =0
max_char=""
for ch in freq:
    if freq[ch]>max_count:
        max_count=freq[ch]
        max_char=ch
print(max_count,"->",max_char)
