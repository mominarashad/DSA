class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

     
        res=[]

        def solve(index,current):

            if len(current)+(n-index+1)<k:
                return None

            if len(current)==k:
                return res.append(current[:])

            if index>n:
                return None

            current.append(index)
            solve(index+1,current)
            current.pop()
            solve(index+1,current)

            return res
        
        return solve(1,[])