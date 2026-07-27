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
# optimal solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1={}
        for i in s:
            count1[i]=count1.get(i,0)+1
        for ch in t:
            if ch not in count1:
                return False
            count1[ch]-=1
            if count1[ch]==0:
                del count1[ch]
        return len(count1)==0
a=Solution()
print(a.isAnagram("anagram","nagaram"))
print(a.isAnagram("rat","car"))
    