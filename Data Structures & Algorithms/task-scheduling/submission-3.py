import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list, p: int) -> int:
        
        #find the frequencies

        freq=Counter(tasks)

        #push in heap

        max_heap=[-count for count in freq.values()]

        #heapify
        heapq.heapify(max_heap)

        #move from max_heap to temp

        time=0

        while max_heap:
            temp=[]

            for _ in range(p+1):
                if max_heap:
                    temp.append(-heapq.heappop(max_heap)-1)

            for freq_left in temp:
                if freq_left>0:
                    heapq.heappush(max_heap,-freq_left)

            if not max_heap:
                time+=len(temp)
            else:
                time+=(p+1)

        return time
