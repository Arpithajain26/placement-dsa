stack=[]
top=-1
size=5
def push():
    global top
    if top==size:
        print("stack size is full")
        return

    
    elm=int(input("enter the elm: "))
    stack.append(elm)
    top+=1
def pop():
    if top==-1:
        print("stack is empty")
        return 

    
    else:
        elm=stack.pop()
        print("poped elm is ",elm)
        top-=1
def display():
    for i in range(top,-1,-1):
        print(stack[i])
while(1):
    print("1.push 2.pop 3.display \n ")
    ch=int(input("enter your choice "))
    if ch==1:
        push()
        
    elif ch==2:
        pop()
       
    elif ch==3:
        display()
     
    else:
        exit()





    
