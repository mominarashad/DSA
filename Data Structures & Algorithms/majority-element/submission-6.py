class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq={}

        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        return max(freq,key=freq.get)
        