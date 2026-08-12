def longest_without_repetation(s):
    max_length=0
    for i in range(len(s)):
        mpp=[0]*256
        for j in range(i,len(s)):
            if mpp[ord(s[j])]==1:
                break
            mpp[ord(s[j])]=1
            length=j-i+1
            max_length=max(max_length,length)
    return max_length
print(longest_without_repetation("abcabcbb"))
