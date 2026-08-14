from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def cycleLength(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                counter=1
                fast=slow.next
                while slow!=fast:
                    fast=fast.next 
                    counter+=1
                return counter
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
