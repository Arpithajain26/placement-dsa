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