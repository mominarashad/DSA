class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res=[]

        intervals.sort(key=lambda x:x[0])

        new_interval=intervals[0]
        res.append(new_interval)

        for interval in intervals:

            if interval[0]<=new_interval[1]:
                new_interval[1]=max(new_interval[1],interval[1])
            else:
                new_interval=interval
                res.append(new_interval)

        return res
        