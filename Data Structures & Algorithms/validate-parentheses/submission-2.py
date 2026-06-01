class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for val in s:
            if val in parent:
                if not stack or stack[-1] != parent[val]:
                    return False
                stack.pop()    
            else:
                stack.append(val)
        return len(stack) == 0                 

        