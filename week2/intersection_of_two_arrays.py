# https://leetcode.com/problems/intersection-of-two-arrays/submissions/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        for num in nums1:
            set1.add(num)
        
        intersection = set()
        for num in nums2:
            if num in set1:
                intersection.add(num)
        
        return [num for num in intersection]