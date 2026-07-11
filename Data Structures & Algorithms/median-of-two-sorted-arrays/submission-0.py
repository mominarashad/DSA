class Solution:
      def findMedianSortedArrays(self,nums1, nums2):
            # Ensure nums1 (smaller) is the smaller array to keep binary search bounded
                smaller = nums1 if len(nums1) <= len(nums2) else nums2
                larger = nums2 if len(nums1) <= len(nums2) else nums1
                totalLength = len(nums1) + len(nums2)

                low, high = 0, len(smaller)

                while low <= high:
                    partitionX = (low + high) // 2
                    partitionY = (totalLength + 1) // 2 - partitionX

                    l1 = float('-inf') if partitionX == 0 else smaller[partitionX - 1]
                    r1 = float('inf') if partitionX == len(smaller) else smaller[partitionX]

                    
                    l2 = float('-inf') if partitionY == 0 else larger[partitionY - 1]
                    r2 = float('inf') if partitionY == len(larger) else larger[partitionY]

                    if l1 <= r2 and l2 <= r1:
                                                                                                    # valid partition
                        if totalLength % 2 == 0:
                            return (max(l1, l2) + min(r1, r2)) / 2.0
                        else:
                            return max(l1, l2)
                    elif l1 > r2:
                        high = partitionX - 1
                    else:
                        low = partitionX + 1

                return 0        