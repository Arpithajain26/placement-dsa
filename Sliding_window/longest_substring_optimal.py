"""Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces."""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength=0
        mpp=[0]*256
        left,right=0,0
        x=len(s)
        while right<x:
            if mpp[ord(s[left])]!=-1:
                if mpp[ord(s[right])]>=left:
                    left=mpp[ord(s[right])]+1
            length=right-left+1
            maxlength=max(maxlength,length)
            mpp[ord(s[right])]=right
            right+=1
        return maxlength

a=Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))