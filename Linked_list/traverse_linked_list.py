"""Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 """
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        temp=head
        while temp!=None:
            stack.append(temp)
            temp=temp.next
        if not stack:
            return None
        head=stack.pop()
        temp=head
        while stack:
            temp.next=stack.pop()
            temp=temp.next
        temp.next=None
        return head
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()

result = solution.reverseList(head)
while result:
    print(result.val,end="->")
    result=result.next

