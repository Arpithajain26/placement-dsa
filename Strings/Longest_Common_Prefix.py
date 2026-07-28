# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word=strs[0]
        for i in range(len(word)):
            for ch in strs[1:]:
                if i==len(ch) or word[i]!=ch[i]:
                    return word[0:i]
        return word
a=Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
