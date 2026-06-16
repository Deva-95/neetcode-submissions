class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def bk(op,cl):

            if op==cl==n:
                res.append("".join(stack))
                return 

            if op<n:
                stack.append('(')
                bk(op+1,cl)
                stack.pop()

            if cl<op:
                stack.append(')')
                bk(op,cl+1)
                stack.pop()
            
        bk(0,0)
        return res
        