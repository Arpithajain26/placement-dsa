# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        temp=head
        while temp:
            stack.append(temp)
            temp=temp.next
        
        temp=head
        while stack:
            ans=stack.pop()
            if temp.val!=ans.val:
                return False
            temp=temp.next
        return True
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

s = Solution()
print(s.isPalindrome(head))

        # stack=[1,2,3,1]

        