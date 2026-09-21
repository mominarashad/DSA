class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first():

            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    ans=mid
                    high=mid-1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1

            return ans

        def last():

            low=0
            high=len(nums)-1
            ans=-1
            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    ans=mid
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1

            return ans

        fir=first()
        las=last()

        return [fir,las]




        

                