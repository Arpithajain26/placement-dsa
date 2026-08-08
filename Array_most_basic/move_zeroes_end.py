def move_zeroes_end(nums):
    i=-1
    for j in range(len(nums)):
        if nums[j]==0:
            i=j
            break
    for  j in range(i+1,len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    return nums


print(move_zeroes_end([0,1,2,0,3,4,0]))