class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n=len(nums)

        for i in range(n):
            if nums[i]<=0 or nums[i]>n:
                nums[i]=n+1

        for ch in nums:
            val=abs(ch)

            if val<=n:
                nums[val-1]=-abs(nums[val-1])

        for idx,ch in enumerate(nums):

            if ch>0:
                return idx+1
        return n+1
                

        