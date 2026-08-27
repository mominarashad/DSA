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


        b=len(buckets)
        res=[]
        for i in range(b-1,-1,-1):
            for bucket in buckets[i]:
                res.append(bucket)
                if len(res)==k:
                    return res
                
            
