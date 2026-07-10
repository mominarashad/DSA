class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap=[]

        n=len(points)

        for i in range(n):

            heapq.heappush(max_heap,(-(points[i][0]**2+points[i][1]**2),-points[i][0],-points[i][1]))

            if len(max_heap)>k:
                heapq.heappop(max_heap)

        return [[-x,-y] for _,x,y in max_heap]

        
          