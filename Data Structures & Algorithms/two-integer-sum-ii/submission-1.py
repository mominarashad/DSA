class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        freq={}

        for idx,val in enumerate(numbers):
            diff=target-val
            if diff in freq:
                return [freq[diff]+1,idx+1]

            freq[val]=idx
        