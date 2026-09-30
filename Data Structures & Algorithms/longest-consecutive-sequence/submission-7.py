class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set=set(nums)
        max_len=float("-inf")
        for ch in num_set:

            if (ch-1) not in num_set:
                length=0

                while ch+length in num_set:
                    length+=1

                max_len=max(max_len,length)

        return max_len if max_len!=float("-inf") else 0