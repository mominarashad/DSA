class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack=[]

        for ch in operations:
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
            elif ch =="+":
                a=stack[-1]
                b=stack[-2]

                stack.append(a+b)
            elif ch=='D':
                stack.append(2*stack[-1])
            else:
                stack.pop()

        return sum(stack)
        