class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curr_max=curr_min=best=nums[0]

        for x in nums[1:]:
            candidates=[x,x*curr_max,x*curr_min]
            curr_max=max(candidates)
            curr_min=min(candidates)
            best=max(best,curr_max)

        return best