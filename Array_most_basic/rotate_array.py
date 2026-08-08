def rotate_array(nums,k):
    num1=[]
    num2=[]
    num1.extend(nums[:k])
    num2.extend(nums[k:])
    num2.extend(num1)
    return num2
print(rotate_array([1,2,3,4,5,6,7],3))
