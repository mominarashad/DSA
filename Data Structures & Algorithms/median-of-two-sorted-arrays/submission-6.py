class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        small=nums1 if len(nums1)<=len(nums2) else nums2
        large=nums2 if len(nums2)>=len(nums1) else nums1

        low=0
        high=len(small)

        total_len=len(nums1)+len(nums2)


        while low<=high:

            part_X=(low+high)//2
            part_Y=(total_len+1)//2-part_X

            l1=float("-inf") if part_X==0 else small[part_X-1]
            r1=float("inf") if part_X==len(small) else small[part_X]

            l2= float("-inf") if part_Y==0 else large[part_Y-1]
            r2=float("inf") if part_Y==len(large) else large[part_Y]

            if l1<=r2 and l2<=r1:

                if total_len%2==0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)

            elif l1>=r2:
                high=part_X-1
            else:
                low=part_X+1

        return 0
            
            