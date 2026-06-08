name = "silent helloi programing"
shortest=""
word=""
result=""
first =True
for ch in name:
    if ch  in " ":
        if first:
            shortest=word
            result=word
            first =False
        elif len(word)< len(shortest):
           shortest=word
           result=word
        elif len(word) == len(shortest):
            result =result +" "+word  
        word=""
    else:
        word+=ch
if first:
     result=word       
elif len(word) <len(shortest):
      result=word    
elif len(word) == len(shortest):
            result =result +" "+word             
        
print("shortest word is  ",result)        


 