s="is2 Th1is an3 exam4ple"

pos=0
words=s.split()
ans=[""]*len(words)
for i in words:
    for j in i:
        if j.isdigit():
            pos=int(j)
            break
    ans[pos-1]=i.replace(str(pos),"")
print(" ".join(ans))

    
