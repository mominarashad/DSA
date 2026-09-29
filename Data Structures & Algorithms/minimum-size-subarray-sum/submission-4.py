class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len=float("inf")

        sum=0
        left=0
        for i in range(len(nums)):

            sum+=nums[i]

            while sum>=target:
                length=i-left+1
                min_len=min(min_len,length)
                sum-=nums[left]
                left+=1

        return min_len if min_len!=float("inf")  else 0  