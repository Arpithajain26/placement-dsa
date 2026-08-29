class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        elm=int(input("enter the new node"))
        newnode=Node(elm)
        newnode.next=self.top
        self.top=newnode

    def pop(self):
        if self.top is None:
            print("stack is empty")
            return
        
        temp=self.top
        self.top=self.top.next
        print(temp.data)

    def display(self):
        temp=self.top
        while temp:
            print(temp.data)
            temp=temp.next


stack = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        stack.push()

    elif ch == 2:
        stack.pop()

    elif ch == 3:
        stack.display()

    elif ch == 4:
        break

    else:
        print("Invalid choice")