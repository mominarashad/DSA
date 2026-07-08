class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack=[]

        for a in asteroids:
            is_alive=True
            while a<0 and is_alive  and stack and stack[-1]>0:

                if stack[-1]<-a:
                    stack.pop()
                    continue
                if stack[-1]==-a:
                    stack.pop()
                is_alive=False

            if is_alive:
                stack.append(a)

        return stack
        