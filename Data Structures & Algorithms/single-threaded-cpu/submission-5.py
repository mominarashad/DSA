import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)

        sorted_tasks=sorted( (tasks[i][0],tasks[i][1],i ) for i in range(n))

        min_heap=[]
        idx=0
        res=[]
        current_time=0
        while min_heap or idx<n:

            if not min_heap and current_time<sorted_tasks[idx][0]:
                current_time=sorted_tasks[idx][0]

            while idx<n and current_time>=sorted_tasks[idx][0]:
                arrival_time,completion_time,original_index=sorted_tasks[idx]
                heapq.heappush(min_heap,(completion_time,original_index))
                idx+=1

            completion_time,original_index=heapq.heappop(min_heap)
            current_time+=completion_time
            res.append(original_index)

        return res

