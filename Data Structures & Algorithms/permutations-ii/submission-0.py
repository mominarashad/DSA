class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n=len(nums)
        res=[]
        is_used=[False]*n

        def solve(current):

            if len(current)==n:
                return res.append(current[:])

            
            for i in range(n):
                if is_used[i]:
                 continue


                if i>0 and nums[i]==nums[i-1] and not is_used[i-1]:
                  continue

                is_used[i]=True
                current.append(nums[i])
                solve(current)
                current.pop()
                is_used[i]=False

            return res
        return solve([])


            

        