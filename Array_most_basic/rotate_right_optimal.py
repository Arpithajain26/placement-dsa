def rotate_array(nums,k):
    nums[k:]=reversed(nums[k:])
    nums[:k]=reversed(nums[:k])
    nums[:]=reversed(nums[:])
    return nums
print(rotate_array([1,2,3,4,5,6,7],3))