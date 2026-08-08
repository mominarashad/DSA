class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=set()

        for ch in nums:
            if ch in freq:
                return True
            else:
                freq.add(ch)

        return False
        