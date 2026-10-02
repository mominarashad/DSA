class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack=[]

        for a in asteroids:

            is_alive=True

            while stack and a<0 and stack[-1]>0 and is_alive:

                if stack[-1]<-a:
                    stack.pop()
                    continue

                elif stack[-1]==-a:
                    stack.pop()

                is_alive=False

            if is_alive:
                stack.append(a)

        return stack

