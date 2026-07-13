class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]

        def solve(index,current):

            if index==n:
                return res.append(current[:])

            current.append(nums[index])
            solve(index+1,current)
            current.pop()

            j=index+1

            while j<n and nums[j]==nums[index]:
                j+=1
                
            solve(j,current)

            return res
        
        return solve(0,[])
        
        