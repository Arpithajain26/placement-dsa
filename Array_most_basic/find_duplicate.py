def find_duplicate(nums):
    mpp={}
    for i in nums:
        mpp[i]=mpp.get(i,0)+1
        for key,value in mpp.items():
            if value>1:
                return key
print(find_duplicate([1, 2, 3, 2, 1]))
