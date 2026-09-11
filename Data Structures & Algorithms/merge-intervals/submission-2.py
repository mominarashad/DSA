class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result=[]

        intervals.sort(key=lambda x:x[0])

        new_interval=intervals[0]
        result.append(new_interval)


        for interval in intervals:

            if interval[0]<=new_interval[1]:
                new_interval[1]=max(interval[1],new_interval[1])
            else:
                new_interval=interval
                result.append(new_interval)

        return result

        