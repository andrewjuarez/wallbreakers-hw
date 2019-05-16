# https://leetcode.com/problems/peak-index-in-a-mountain-array/solution/

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left_index = 0
        right_index = len(A) - 1
        
        while left_index < right_index:
            center = (left_index + right_index) // 2
            if(A[center] < A[center + 1]):
                left_index = center + 1
            else:
                right_index = center
            
        return left_index
    