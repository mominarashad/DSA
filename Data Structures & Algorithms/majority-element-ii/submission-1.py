class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n=len(nums)

        freq={}

        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        res=[]

        for ch,values in freq.items():
            if values>(n//3):
                res.append(ch)
        return res
        