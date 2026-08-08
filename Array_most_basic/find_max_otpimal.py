def max_sum(nums):
    max_element=nums[0]
    for i in range(len(nums)):
        if nums[i]>max_element:
            max_element=nums[i]
    return max_element
print(max_sum([4,5,4,3,2,345,6]))