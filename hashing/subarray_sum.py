"""Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2"""
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mpp={0:1}
        count=0
        sum=0
        for num in nums:
            sum+=num
            if sum-k in mpp:
                count+=mpp[sum-k]
            mpp[sum]=mpp.get(sum,0)+1
        return count
a=Solution()
print(a.subarraySum([1,1,1],2))