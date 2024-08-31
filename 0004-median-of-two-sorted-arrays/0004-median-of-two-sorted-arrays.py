class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_arr = sorted(nums1+nums2)
        size = len(merged_arr)
        if size % 2 != 0:
            index = (size+1)//2
            median = merged_arr[index-1]
            return median
        elif size % 2 == 0:
            index_one = ((size//2)+1)
            index_two = (size//2)
            median = (merged_arr[index_one-1]+merged_arr[index_two-1])/2.0
            return median
