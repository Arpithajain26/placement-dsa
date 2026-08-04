def longest(nums):
    nums.sort()
    last_smaller=float('-inf')
    count=0
    longest=1
    for i in range(len(nums)):
        if nums[i]-1==last_smaller:
            count+=1
            last_smaller=nums[i]
        elif nums[i]!=last_smaller:
            count=1
            last_smaller=nums[i]
        longest=max(longest,count)
    return longest
nums=[100,4,200,1,3,2]
print(longest(nums))