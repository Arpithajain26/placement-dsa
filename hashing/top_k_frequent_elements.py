"""347. Top K Frequent Elements
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, 
return the k most frequent elements.
 You may return the answer in any order."""
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups={}
        ans=[]
        for i in nums:
         
            groups[i]=groups.get(i,0)+1
        sorted_items=sorted(groups.items(),key=lambda x:x[1],reverse=True)
        for key,value in sorted_items[:k]:
            ans.append(key)
        return ans
a=Solution()
print(a.topKFrequent([1,1,1,2,2,3],k=2))

