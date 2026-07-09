import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        # Attach original index, then sort by start time
        # sortedTasks[i] = (start_time, processing_time, original_index)
        sortedTasks = sorted(
            [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        )  # O(n log n)

        result = []
        curr_time = 0
        idx = 0

        # Min-heap of (processing_time, original_index)
        # Python tuples compare lexicographically, so ties on processing_time
        # break by smaller index — exactly what the problem asks for.
        pq = []

        while idx < n or pq:

            # CPU is idle: jump forward to the next task's start time
            if not pq and curr_time < sortedTasks[idx][0]:
                curr_time = sortedTasks[idx][0]

            # Push every task that has become available by curr_time
            while idx < n and sortedTasks[idx][0] <= curr_time:
                start_time, processing_time, original_index = sortedTasks[idx]
                heapq.heappush(pq, (processing_time, original_index))  # O(log n)
                idx += 1

            # Pick the shortest available task (ties: smaller index)
            proc_time, original_index = heapq.heappop(pq)
            curr_time += proc_time
            result.append(original_index)

        return result
        # Time:  O(n log n)
        # Space: O(n)