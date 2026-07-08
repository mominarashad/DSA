class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heaps=nums
        heapq.heapify(self.heaps)
        while len(self.heaps)>self.k:
            heapq.heappop(self.heaps)
        

    def add(self, val: int) -> int:

        if len(self.heaps)<self.k:
            heapq.heappush(self.heaps,val)
        elif val>self.heaps[0]:
            heapq.heapreplace(self.heaps,val)
        return self.heaps[0]



        
