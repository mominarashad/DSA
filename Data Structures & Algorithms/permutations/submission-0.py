class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]

        def solve(index):

            if index==n:
                return res.append(nums[:])

            for i in range(index,n):
                nums[index],nums[i]=nums[i],nums[index]
                solve(index+1)
                nums[index],nums[i]=nums[i],nums[index]

            return res
        return solve(0)
