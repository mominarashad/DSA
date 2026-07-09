import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)

        sorted_tasks=sorted([ (tasks[i][0],tasks[i][1],i) for i in range(n)])

        result=[] # to put index for output
        curr_time=0
        min_heap=[]

        index=0

        while min_heap or index<n:
            
            if not min_heap and curr_time<sorted_tasks[index][0]:
                curr_time=sorted_tasks[index][0]

            while index<n and sorted_tasks[index][0]<=curr_time:
                arrival_time,comp_time,i=sorted_tasks[index]
                heapq.heappush(min_heap,(comp_time,i))
                index+=1

            comp_time,i=heapq.heappop(min_heap)

            curr_time+=comp_time
            result.append(i)

        return result
