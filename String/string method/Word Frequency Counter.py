word=input("Enter Your word: ")
freq={}

for word in word.split():
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
        
print(freq)        