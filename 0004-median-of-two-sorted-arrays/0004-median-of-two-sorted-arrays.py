class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = (nums1 + nums2)
        merged_arr.sort()
        size = len(merged_arr)
        
        if size % 2 != 0:
            index = size // 2
            return float(merged_arr[index])
        else:
            mid2 = (size // 2) + 1
            mid1 = size // 2
            return (merged_arr[mid1-1] + merged_arr[mid2-1]) / 2.0