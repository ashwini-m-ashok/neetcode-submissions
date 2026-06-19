class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+-/*'):
                if token == '+':
                    stack.append(stack.pop()+stack.pop())
                if token == '-':
                    val2=stack.pop()
                    val1=stack.pop()
                    stack.append(val1-val2)
                if token == '*':
                    stack.append(stack.pop()*stack.pop())
                if token == '/':
                    val2=stack.pop()
                    val1=stack.pop()
                    stack.append(int(val1/val2))
            else:
                stack.append(int(token))
        
        return stack[-1] if stack else 0