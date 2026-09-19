class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def count_array(array_sum):

            sub_array=1
            load=0

            for num in nums:
                if load+num > array_sum:
                    sub_array+=1
                    load=0

                load+=num

            return sub_array<=k

        low=max(nums)
        high=sum(nums)

        while low<high:
            mid=(low+high)//2

            if count_array(mid):
                high=mid
            else:
                low=mid+1
        return low
        