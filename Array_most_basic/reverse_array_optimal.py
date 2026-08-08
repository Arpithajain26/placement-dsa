def reverse_array_optimal(nums):
    num=[]
    for i in range(len(nums)-1,-1,-1):
        num.append(nums[i])
    return num
print(reverse_array_optimal([1,2,3,4,5,6,7,8]))