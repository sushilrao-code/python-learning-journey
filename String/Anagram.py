s1 = "slient"
s2="listen"
anagram=True

for ch in s1:
    if ch in s2:
        s2=s2.replace(ch,"",1)
    else:
        anagram=False
            
if s2 !="":
    anagram=False

if anagram:
    print("Anagram")
else:
    print("Not Anagram")        