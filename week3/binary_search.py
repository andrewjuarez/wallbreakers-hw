# https://leetcode.com/problems/binary-search/submissions/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        
        while left_index <= right_index:
            center = (right_index + left_index) // 2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left_index = center + 1
            else:
                right_index = center - 1
            
        return -1