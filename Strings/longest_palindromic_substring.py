# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.
def longest_palindrome_substring(s):
    ans=""
    for i in range(len(s)):
        right=left=i
        while left>=0 and right<len(s) and s[left]==s[right]:
            if right-left+1 >len(ans):
                ans=s[left:right+1]
            left-=1
            right+=1


        left=i
        right=i+1
        while left>=0 and right<len(s) and s[left]==s[right]:
            if right-left+1>len(s):
                ans=s[left:right+1]
            left-=1
            right+=1
    return ans
print(longest_palindrome_substring("racecarmm"))
print(longest_palindrome_substring("aceca"))


