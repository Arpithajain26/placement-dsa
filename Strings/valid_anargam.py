# 242. Valid Anagram
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1={}
        for i in t:
            if i in count1:
                count1[i]+=1
            else:
                count1[i]=1
        count2={}
        for i in s:
            if i in count2:
                count2[i]+=1
            else:
                count2[i]=1
        return count1==count2


a=Solution()
print(a.isAnagram("anagram","nagaram"))
print(a.isAnagram("rat","car"))