def second_largest(nums):
    max_elm=max(nums)
    min_elm=nums[0]
    for i in range(len(nums)):
        if nums[i]>min_elm and nums[i]<max_elm:
            min_elm=nums[i]
    return min_elm
print(second_largest([1,2,3,4,5,6]))