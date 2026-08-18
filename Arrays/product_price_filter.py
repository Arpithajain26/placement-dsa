s={"Laptop":"55000","Phone":"25000", "Mouse":"800"," Keyboard":"1500"}
ans=[]
for key,value in s.items():
    if int(value)>20000:
        ans.append(key)
print(" ".join(ans))