class Solution:
    def decodeString(self, s: str) -> str:

        num_stack=[]
        ch_stack=[]

        curr=""
        num=0

        for ch in s:
            
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=='[':
                num_stack.append(num)
                ch_stack.append(curr)

                curr=""
                num=0

            elif ch==']':
                k=num_stack.pop()
                val=ch_stack.pop()

                curr=val+curr*k

            else:
                curr+=ch

        return curr

        