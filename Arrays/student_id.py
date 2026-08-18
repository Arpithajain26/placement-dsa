s="STU101 CSE202 STU103 STU12 STU999"
ans=[]
words=s.split()
for word in words:
    if len(word)==6 and word.startswith('STU') and word[3:6].isdigit():
        ans.append(word)
print(ans)