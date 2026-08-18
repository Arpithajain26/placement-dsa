s="Hello123 password ABCdef12 Test@123"
words=s.split()
ans=[]
for word in words:
    has_digit=False
    has_lower=False
    has_upper=False
    if len(word)>=8:
        for ch in word:
            if ch.isdigit():
                has_digit=True
            elif ch.isupper():
                has_upper=True
            elif ch.islower():
                has_lower=True
    if has_lower and has_upper and has_digit:
        ans.append(word)
print(" ".join(ans))