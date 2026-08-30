def reverse_string(s):
    return s[::-1]
print(reverse_string("apsara"))
def check_palindrome(s):
    return s==s[::-1]
print(check_palindrome("madam"))
def count_frequency(s):
    mpp={}
    for i in s:
        mpp[i]=mpp.get(i,0)+1
    return mpp
print(count_frequency("hello"))
def check_anargam(s,t):
   mpp1={}
   mpp2={}
   for i in s:
       mpp1[i]=mpp1.get(i,0)+1
   for j in t:
       mpp2[j]=mpp2.get(j,0)+1
   return mpp1==mpp2
print(check_anargam("listen","silent"))
def find_duplicated(nums):
    mpp={}
    num=[]
    for i in nums:
        mpp[i]=mpp.get(i,0)+1
    for key,value in mpp.items():
        if value>1:
            num.append(key)
    return num

print(find_duplicated([1,2,3,2,4,2]))
def second_largest(nums):
    max_elm=max(nums)
    nums.remove(max_elm)
    return max(nums)
print(second_largest([10,5,8,20,15]))
def missing_nums(nums,n):
    sum_of_n=n*(n+1)//2
    sum_n=sum(nums)
    return sum_of_n-sum_n
print(missing_nums([1,2,3,5],5))
def remove_duplicates(nums):
    return list(set(nums))
print(remove_duplicates([1,2,2,3,3,4]))
def move_zeroes(nums):
    i=0
    for j in range(len(nums)):
        if nums[j]==0:
            i=j
            break
    for j in range(i+1,len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    return nums
print(move_zeroes([0,1,0,3,12]))
def two_sum(nums,target):
    mpp={}
    for i in nums:
        num=target-i
        if num in mpp:
            return [i,mpp[num]]
        mpp[num]=i
    return
print(two_sum([2,7,11,15],9))




