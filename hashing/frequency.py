def majority_element(nums):
    n=len(nums)
    for i in range(len(nums)):
        count=0
        for j in range(i,len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count>(n//2):
            return nums[i]
nums=[2,2,3,3,1,2,2]
print(majority_element(nums))


# optimal solution
def majority_element1(nums):
    n=len(nums)
    mpp={}
    for num in nums:
        mpp[num]=mpp.get(num,0)+1
    for key,value in mpp.items():
        if value>n//2:
            return key

nums=[2,2,3,3,1,2,2]
print(majority_element1(nums))

# optimal solution

    
    
