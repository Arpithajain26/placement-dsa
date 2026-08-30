def infix_to_postfix_exp(s):
    stack=[]
    ans=[]
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    for ch in s:
        if ch.isalpha():
            stack.append(ch)
        elif ch=='(':
            ans.append(ch)
        elif ch==')':
            
            while ans and ans[-1]!='(':
                a=ans.pop()
                stack.append(a)
            ans.pop()
        else:

            while ( ans and ans[-1]!='(' and precedence[ans[-1]]>precedence[ch]):
                stack.append(ans.pop()) 
            ans.append(ch)
        while ans:
            stack.append(ans.pop())
    return "".join(stack)    

print(infix_to_postfix_exp("A+B*C"))
print(infix_to_postfix_exp("(A+B)*C"))
print(infix_to_postfix_exp("A*B+C/D"))