class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        seen=defaultdict(int)
        seen[0]=1
        prefix=0
        count=0

        for ch in nums:
            prefix+=ch
            count+=seen[prefix-k]
            seen[prefix]+=1

        return count
        