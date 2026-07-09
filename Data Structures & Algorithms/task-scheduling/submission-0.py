import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list, p: int) -> int:
        freq = Counter(tasks)
        
        # max heap (negate values since heapq is a min heap)
        pq = [-count for count in freq.values()]
        heapq.heapify(pq)
        
        time = 0
        
        while pq:
            temp = []
            for _ in range(p + 1):
                if pq:
                    temp.append(-heapq.heappop(pq) - 1)  # finish one instance
            
            for freq_left in temp:
                if freq_left > 0:
                    heapq.heappush(pq, -freq_left)
            
            if not pq:
                time += len(temp)
            else:
                time += (p + 1)
        
        return time