class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set=set(nums)
        max_len=0
        for ch in nums:
            if (ch-1) not in num_set:
                length=0
                while (ch+length) in num_set:
                    length+=1
                max_len=max(max_len,length)

        return max_len