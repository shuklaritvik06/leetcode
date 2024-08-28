class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = sorted(nums1 + nums2)
        size = len(sorted_arr)
        
        if size % 2 != 0:
            index = size // 2
            return float(sorted_arr[index])
        else:
            mid2 = (size // 2) + 1
            mid1 = size // 2
            return (sorted_arr[mid1-1] + sorted_arr[mid2-1]) / 2.0