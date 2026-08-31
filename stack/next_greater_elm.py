def majority_elem(nums):
    stack=[]
    ans=[-1]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        while stack and stack[-1]<=nums[i]:
            stack.pop()
        if stack:
            ans[i]=stack[-1]
        else:
            stack.append(nums[i])
    return ans
print(majority_elem([6,0,8,1,3]))