class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        left_mul=[1]*n
        right_mul=[1]*n

        for i in range(1,n):
            left_mul[i]=nums[i-1]*left_mul[i-1]

        for i in range(n-2,-1,-1):
            right_mul[i]=nums[i+1]*right_mul[i+1]

        return [left_mul[i]*right_mul[i] for i in range(n)]

        