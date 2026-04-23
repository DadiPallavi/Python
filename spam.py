s="paaallavi"
count=1
for i in range(1,len(s)-1):
    if s[i]==s[i+1]:
        count+=1
        if count==3:
            print("Spam")
    else:
        count=1
else:
    print("not Spam")