mpp={
    "Arun": "P",
    "Ravi": "A",
    "Meena": "P",
    "John": "A",
    "Priya": "P"
}
ans=[]
for key,value in mpp.items():
    if value=="P":
        ans.append(key)
print(" ".join(ans))