class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_heap=[]
        res=[]
        if a>0:
            heapq.heappush(max_heap,(-a,'a'))
        if b>0:
            heapq.heappush(max_heap,(-b,'b'))
        if c>0:
            heapq.heappush(max_heap,(-c,'c'))

        while max_heap:

            current_count,current_char=heapq.heappop(max_heap)
            current_count=-current_count

            if len(res)>=2 and res[-1]==current_char and res[-2]==current_char:
                if not max_heap:
                    break

                nxt_count,nxt_char=heapq.heappop(max_heap)
                nxt_count=-nxt_count

                res.append(nxt_char)
                nxt_count-=1

                if nxt_count>0:
                    heapq.heappush(max_heap,(-nxt_count,nxt_char))

                heapq.heappush(max_heap,(-current_count,current_char))
            else:
                res.append(current_char)
                current_count-=1

                if current_count>0:
                    heapq.heappush(max_heap,(-current_count,current_char))

        return "".join(res)


                