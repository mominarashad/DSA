import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)

        sorted_task=sorted([(tasks[i][0],tasks[i][1],i) for i in range(n)])

        res=[]
        current_time=0
        idx=0
        min_heap=[]

        while min_heap or idx<n:

            if not min_heap and current_time<sorted_task[idx][0]:
                current_time=sorted_task[idx][0]

            while idx<n and sorted_task[idx][0]<=current_time:
                arrival_time,completion_time,original_index=sorted_task[idx]
                heapq.heappush(min_heap,(completion_time,original_index))
                idx+=1

            completion_time,original_index=heapq.heappop(min_heap)
            current_time+=completion_time
            res.append(original_index)

        return res