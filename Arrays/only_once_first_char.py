s="swiss"
mpp={}
for i in s:
    mpp[i]=mpp.get(i,0)+1
for key,value in mpp.items():
    if value==1:
        print(key)
        break