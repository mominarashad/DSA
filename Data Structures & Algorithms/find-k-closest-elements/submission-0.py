class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap=[]

        n=len(arr)

        for i in range(n):
            heapq.heappush(max_heap,(-abs(arr[i]-x),-arr[i]))

            if len(max_heap)>k:
                heapq.heappop(max_heap)

        result= [-x for _,x in max_heap]
        result.sort()
        return result
