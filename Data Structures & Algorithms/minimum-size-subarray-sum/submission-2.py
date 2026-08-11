class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        left=0

        min_len=float("inf")
        sum=0
        for right in range(len(nums)):
            sum+=nums[right]

            while sum>=target:
                length=right-left+1
                min_len=min(min_len,length)
                sum-=nums[left]
                left+=1

    
        return (0 if min_len==float("inf") else min_len)

        