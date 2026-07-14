class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}

        for ch in nums:
            if ch in freq:
                freq[ch]+=1

            else:
                freq[ch]=1

        buckets=[[] for _ in range(len(nums)+1)]

        for val,count in freq.items():
            buckets[count].append(val)
        
        res=[]

        for i in range(len(buckets)-1,-1,-1):
            for bucket in buckets[i]:
                res.append(bucket)
                if len(res)==k:
                    return res

        