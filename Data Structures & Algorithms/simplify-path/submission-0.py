class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack=[]
        parts=path.split('/')
        for ch in parts:

            if ch =="" or ch ==".":
                continue
            elif ch=="..":
                if stack:
                   stack.pop()
            else:
                stack.append(ch)

        return '/'+'/'.join(stack)