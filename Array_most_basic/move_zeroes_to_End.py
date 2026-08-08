def move_zeroes_end(nums):
    num=[]
    for i in range(len(nums)):
        if nums[i]==0:
            num.append(nums[i])
    for x in nums:
        nums.remove(x)
    nums.extend(num)
    return nums
print(move_zeroes_end([1,2,0,3,5,0,6,4,0]))