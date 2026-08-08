def min_element(nums):
    min_elm=nums[0]
    for i in range(len(nums)):
        if nums[i]<min_elm:
            min_elm=nums[i]
    return min_elm
print(min_element([4,6,4,3,4556,65]))