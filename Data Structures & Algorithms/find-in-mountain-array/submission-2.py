class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        def find_peak():

            low=0
            high=n-1

            while low<high:
                mid=(low+high)//2

                if mountainArr.get(mid)<mountainArr.get(mid+1):
                    low=mid+1
                else:
                    high=mid

            return low

        def binary_search(low,high):

            while low <= high:
                mid=(low+high)//2

                if mountainArr.get(mid)==target:
                    return mid

                elif mountainArr.get(mid)>target:
                    high=mid-1
                else:
                    low=mid+1
            return -1

        def reverse_binary_search(low,high):

            while low <= high:
                mid=(low+high)//2

                if mountainArr.get(mid)==target:
                    return mid

                elif mountainArr.get(mid)>target:
                    low=mid+1
                    
                else:
                    high=mid-1
                    
            return -1

        
        peak=find_peak()

        idx=binary_search(0,peak)
        if idx!=-1:
            return idx

        return reverse_binary_search(peak,n-1)
        

        

            
        