class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        smaller=nums1 if len(nums1)<=len(nums2) else nums2
        larger=nums2 if len(nums2)>=len(nums1) else nums1

        total_len=len(nums1)+len(nums2)

        low=0
        high=len(smaller)

        while low<=high:

            partX=(low+high)//2
            partY=((total_len+1)//2)-partX

            l1=float("-inf") if partX==0 else smaller[partX-1]
            r1=float("inf") if partX==len(smaller) else smaller[partX]

            l2=float("-inf") if partY==0 else larger[partY-1]
            r2=float("inf") if partY==len(larger) else larger[partY]

            if l1<=r2 and l2<=r1:

                if total_len%2==0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)
            
            elif l1>=r2:
                high=partX-1
            else:
                low=partX+1

        return 0



        