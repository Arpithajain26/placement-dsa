"""For today, do these coding questions first

Must-do:

Two Sum
Reverse a String
Palindrome
Anagram
Character Frequency
Find Duplicates
Second Largest Element
Maximum Element
Remove Duplicates
Missing Number
Move Zeroes
Maximum Subarray
Best Time to Buy and Sell Stock
Binary Search
Array Rotation
Then revise these patterns

Hashing

dict
set
Counter

Two Pointers

Palindrome
Two Sum (sorted array)

Sliding Window

Maximum sum of size k
Longest substring without repeating characters

Basic sorting/searching

Linear search
Binary search
sort() / sorted()
Two Sum
Maximum Subarray
Best Time to Buy/Sell Stock
Valid Anagram
Valid Palindrome
Longest Substring Without Repeating Characters
Group Anagrams
Longest Consecutive Sequence
Binary Search
Valid Parentheses"""
def reverse(s):
    return s[::-1]
def anargam(s,t):
    mpp1={}
    mpp2={}
    for i in range(len(s)):
        mpp1[s[i]]=mpp1.get(s[i],0)+1
    for j in range(len(t)):
        mpp2[t[j]]=mpp2.get(t[j],0)+1
    return mpp1==mpp2
# print(anargam("arpitha","arihanth"))
def character_frequency(s):
    mpp={}
    for i in range(len(s)):
        mpp[s[i]]=mpp.get(s[i],0)+1
    return mpp
# print(character_frequency("Arpitha"))
def find_duplicates(nums):
    mpp={}
    for num in nums:
        mpp[num]=mpp.get(num,0)+1
    ans=[]
    for key,value in mpp.items():
        if value>1:
            ans.append(key)
    return ans
print(find_duplicates( [4,3,2,7,8,2,3,1]))

def second_largest(nums):
    first=max(nums)
    second=nums[0]
    for i in range(len(nums)):
        if nums[i]<first and nums[i]>second:
            second=nums[i]
    return second
# print(second_largest([1,2,3,4,5,6]))
def max_elem(nums):
    return max(nums)
# print(max_elem([1,2,3,4,5,6]))
def remove_duplicates(nums):
    num1=[]
    for i in range(len(nums)):
        if nums[i] not in num1:
            num1.append(nums[i])
    return num1
print(remove_duplicates([1,1,2,2,3,3,4,5,5,6,7]))
def missing_number(nums,n):
    return (n*(n+1)//2)-sum(nums)
print(missing_number([1,2,3,4,5,7],7))
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
print(move_zeroes([1,0,20,3,0,0,4]))
def max_subarray(nums):
    max_sub=float('-inf')
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            max_sub=max(max_sub,sum)
    return max_sub
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
def max_subarray1(nums):
    sum=0
    maxi=float('-inf')
    for i in range(len(nums)):
        sum+=nums[i]
        maxi=max(maxi,sum)
        if sum<0:
            sum=0
    if maxi<0:
        return -1
    return maxi
print(max_subarray1([-2,1,-3,4,-1,2,1,-5,4]))
def best_time_seel(nums):
    profit=0
    n=nums[0]
    for i in range(len(nums)):
        cost=nums[i]-n
        profit=max(profit,cost)
        n=min(n,nums[i])
    return profit
print(best_time_seel([7,1,5,3,6,4]))
def binay_search(nums,left,right,k):
    mid=(left+right)//2

    if nums[mid]==k:
        return mid
    elif nums[mid]>k:
        return binay_search(nums,left,mid-1,k)
    else:
        return binay_search(nums,mid+1,right,k)
print(binay_search([1, 3, 5, 7, 9],0,5,7))
def array_rotation(nums,k):
    nums[:]=reversed(nums[:])
    nums[:k]=reversed(nums[:k])
    nums[k:]=reversed(nums[k:])
   
  
    return nums
print(array_rotation([1, 2, 3, 4, 5],2))
def maxi_sum(nums,k):
    window=nums[:k]
    left=0
    current_window=sum(window)
    maxi=current_window
    for right in range(k,len(nums)):
        current_window=current_window-nums[left]+nums[right]
        left+=1
        maxi=max(maxi,current_window)
    return maxi
print(maxi_sum([2, 1, 5, 1, 3, 2],3))


    
