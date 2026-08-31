def next_greater_elm(nums):
    ans=[-1]*len(nums)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]>nums[i]:
                ans[i]=nums[j]
                break
        for k in range(0,i):
            if nums[k]>nums[i]:
                ans[i]=nums[k]
                break
    return ans
print(next_greater_elm([2,10,12,1,11]))

