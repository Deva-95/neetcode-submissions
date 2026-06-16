class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opset = ('+','-','*','/')
        for x in tokens:
            if x not in opset:
                stack.append(int(x))
            else:
                opr1 = int(stack.pop())
                opr2 = int(stack.pop())
                if x == "+":
                    stack.append(opr1 + opr2)
                if x == "-":
                    stack.append(opr2 - opr1)
                if x == "*":
                    stack.append(opr1 * opr2)
                if x == "/":
                    stack.append(int(float(opr2) / opr1))
                
        return stack[0]