class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        freq={}

        for idx,ch in enumerate(numbers):
            diff=target-ch

            if diff in freq:
                return [freq[diff]+1,idx+1]

            freq[ch]=idx