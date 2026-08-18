s="Laptop3 Phone1 Mouse2 Keyboard4"
words=s.split()
j=0
ans=[""]*len(words)
for word in words:
    for ch in word:
        if ch.isdigit():
            j=int(ch)
            break
    ans[j-1]=word.replace(str(j),"")
print(" ".join(ans))