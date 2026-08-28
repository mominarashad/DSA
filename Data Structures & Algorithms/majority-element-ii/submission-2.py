class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res=[]
        freq={}
        n=len(nums)
        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1


        for ch,fre in freq.items():
            if fre>(n/3):
                res.append(ch)

        return res
        
