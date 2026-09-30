class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n=len(nums)
        freq={}

        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        buckets=[[] for _ in range(n+1)]

        for ch,fre in freq.items():
            buckets[fre].append(ch)

        res=[]
        for i in range(len(buckets)-1,0,-1):
            for buck in buckets[i]:
                res.append(buck)

                if len(res)==k:
                    return res