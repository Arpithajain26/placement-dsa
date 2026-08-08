def second_largest_element(nums):
    max_elm=max(nums)
    nums.remove(max_elm)
    return max(nums)
print(second_largest_element([1,2,3,4,5,6]))