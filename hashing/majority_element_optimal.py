def majority_element(nums):
    count=0
    for i in range(len(nums)):
        if count==0:
            count+=1
            elm=nums[i]
        elif elm==nums[i]:
            count+=1
        else:
            count-=1
    count1=0
    for i in range(len(nums)):
        if nums[i]==elm:
            count1+=1
    if count1>(len(nums)//2):
        return elm
nums=[2,2,3,3,1,2,2]
print(majority_element(nums))
