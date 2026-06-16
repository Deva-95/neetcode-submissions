class Solution:
    def isValid(self, strs: str) -> bool:
        stack = []
        d = {')':'(',']':'[','}':'{'}
        for s in strs:
            if s in d:
                if stack and stack[-1]==d[s]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(s)
        
        return True if not stack else False