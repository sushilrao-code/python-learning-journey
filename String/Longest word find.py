name = "silent hello programing"
longest=""
word=""
result=""
for ch in name:
    if ch  in " ":
        if len(word)> len(longest):
            longest=word
            result=word
        elif len(word) == len(longest):
            result =result +" "+word     
        word=""
    else:
        word+=ch
if len(word) >len(longest):
          result=word
elif len(word) == len(longest):
            result =result +" "+word                    
        
print("Longest word is  ",result)        


 