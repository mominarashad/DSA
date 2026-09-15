class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        m_map={')':'(','}':'{',']':'['}

        for ch in s:

            if ch in m_map.values():
                stack.append(ch)
            elif ch in m_map:
                if not stack or m_map[ch]!=stack[-1]:
                    return False

                stack.pop()

        return not stack

                
        