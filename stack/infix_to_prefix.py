def infix_to_prefix_exp(s):
    stack = []
    ans = []

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    for ch in reversed(s):

        if ch.isalpha():
            stack.append(ch)

        elif ch == ')':
            ans.append(ch)

        elif ch == '(':
            while ans and ans[-1] != ')':
                stack.append(ans.pop())
            ans.pop()

        else:
            while ans and ans[-1] != ')' and precedence[ans[-1]] > precedence[ch]:
                stack.append(ans.pop())

            ans.append(ch)

    while ans:
        stack.append(ans.pop())

    return "".join(reversed(stack))


print(infix_to_prefix_exp("A+B*C"))
print(infix_to_prefix_exp("(A+B)*C"))
print(infix_to_prefix_exp("A*B+C/D"))