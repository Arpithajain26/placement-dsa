class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
def array_to_linkedlist(arr):
    head=Node(arr[0])
    current=head
    for i in range(1,len(arr)):
        current.next=Node(arr[i])
        current=current.next
    return head
def print_linkedlist(head):
    current=head
    while current:
        print(current.data)
        current=current.next
arr = [10, 20, 30, 40, 50]

head = array_to_linkedlist(arr)
print_linkedlist(head)
