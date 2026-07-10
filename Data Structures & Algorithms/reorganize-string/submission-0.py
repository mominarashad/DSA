class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = [(-count, val) for val, count in freq.items()]
        heapq.heapify(max_heap)

        prev_char = ''
        prev_count = 0
        res = []
        while max_heap:
            count, char = heapq.heappop(max_heap)
            count = -count

            res.append(char)

            if prev_count > 0:
                heapq.heappush(max_heap, (-prev_count, prev_char))

            count -= 1
            prev_char, prev_count = char, count

        result = "".join(res)
        return result if len(result) == len(s) else ""