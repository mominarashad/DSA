class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def subarray_sum(max_sum):

            subarray=1
            load=0

            for w in nums:

                if (load+w)>max_sum:
                    subarray+=1
                    load=0

                load+=w

            return  subarray<=k

        low=max(nums)
        high=sum(nums)

        while low <high:
            mid=(low+high)//2

            if subarray_sum(mid):
                high=mid
            else:
                low=mid+1
        return low
        
        