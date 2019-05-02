# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i < len(digits):
            #print("checking digit", digits[i])
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0
            
            
            
            if i == 0:
                return [1] + digits
            i = i - 1
        return digits        
        