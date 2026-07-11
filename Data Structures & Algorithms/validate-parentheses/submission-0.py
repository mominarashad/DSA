class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        my_map={')':'(',']':'[','}':'{'}

        for ch in s:

            if ch in my_map.values():
                stack.append(ch)
            elif ch in my_map:
                if not stack or stack[-1]!=my_map[ch]:
                    return False
                
                stack.pop()

        return not stack

        