from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mpp={}
        temp=head
        while temp!=None:
            if temp in mpp:
                return temp
            mpp[temp]=1
            temp=temp.next
head = ListNode(4)
node = ListNode(5)
node1 = ListNode(1)
node2 = ListNode(9)

head.next = node
node.next = node1
node1.next = node2

# Create cycle: 9 → 1
node2.next = node1

a = Solution()

result = a.detectCycle(head)

if result:
    print(result.val)
else:
    print("None")