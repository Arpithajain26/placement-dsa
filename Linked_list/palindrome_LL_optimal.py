# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self,head):
        prev=None
        current=head
        while current:
            next_node=current.next 
            current.next=prev 
            prev=current 
            current=next_node 
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next 
        newnode=self.reverse(slow.next)
        first=head 
        second=newnode 
        while second!=None:
            if (first.val!=second.val):
                self.reverse(newnode)
                return False
            first=first.next
            second=second.next 
        self.reverse(newnode)  
        return True 

            
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

s = Solution()
print(s.isPalindrome(head))

        # stack=[1,2,3,1]

        