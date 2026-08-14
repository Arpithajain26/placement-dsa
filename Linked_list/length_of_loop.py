from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def cycleLength(self, head: Optional[ListNode]) -> int:
        mpp={}
        temp=head
        timer=1
        while temp:
            if temp in mpp:
                value=mpp[temp]
                return timer-value
            mpp[temp]=1
            temp=temp.next
            timer+=1
        return 0
head = ListNode(4)
node = ListNode(5)
node1 = ListNode(1)
node2 = ListNode(9)

head.next = node
node.next = node1
node1.next = node2
node2.next = node1

a = Solution()

print(a.cycleLength(head))  
