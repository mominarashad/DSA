class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        has_dup=set()

        for ch in nums:
            if ch in has_dup:
                return True
            
            has_dup.add(ch)

        return False
        