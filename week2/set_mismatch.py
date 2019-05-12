# https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated = 0
        missing = 0
        
        current_nums = set()
        
        for num in nums:
            if num in current_nums:
                repeated = num
            else:
                current_nums.add(num)
        
        for num in range(1, len(nums) + 1):
            if num not in current_nums:
                missing = num
                break
        
        return [repeated, missing]