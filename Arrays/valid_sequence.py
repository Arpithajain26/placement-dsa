s = "AB123x cd456m XYZ12a PQ456z XY789P"

words = s.split()

ans = []

for word in words:
    if word[:2].isupper() and word[2:5].isdigit() and word[-1].islower():
        ans.append(word)
print(" ".join(ans))

