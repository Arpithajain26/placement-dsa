def remove_duplicates_optimal(nums):

    num=[]
    for i in range(len(nums)):
        if nums[i] not in num:
            num.append(nums[i])
    return num
print(remove_duplicates_optimal([1,1,2,3,4,4]))
