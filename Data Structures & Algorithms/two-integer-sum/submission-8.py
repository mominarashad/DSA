class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq={}

        for idx,ch in enumerate(nums):
            diff=target-ch
            if diff in freq:
                return [freq[diff],idx]
            freq[ch]=idx

        
            

        
        