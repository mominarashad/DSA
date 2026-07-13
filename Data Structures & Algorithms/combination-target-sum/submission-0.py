class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n=len(nums)

        res=[]

        def solve(index,current,current_sum):

            if current_sum==target:
                return res.append(current[:])

            if index==n or current_sum>target:
                return None

            current.append(nums[index])
            solve(index,current,current_sum+nums[index])
            current.pop()
            solve(index+1,current,current_sum)

        solve(0,[],0)

        return res
        