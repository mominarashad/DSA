class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def count_array(nums,mid):

            sub_array=1
            load=0

            for ch in nums:
                if load+ch>mid:
                    sub_array+=1
                    load=0
                load+=ch

            return sub_array<=k


        low=max(nums)
        high=sum(nums)

        while low<high:

            mid=(low+high)//2

            if count_array(nums,mid):
                high=mid
            else:
                low=mid+1

        return low