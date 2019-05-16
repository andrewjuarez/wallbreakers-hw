# https://leetcode.com/problems/lemonade-change/description/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = {5:0, 10:0, 20:0}
        
        for bill in bills:
            bank[bill] += 1
            
            change = bill - 5
            
            #while change > 0:
            if change >= 10:
                if bank[10] > 0:
                    bank[10] -= 1
                    change -= 10
            if change >= 5:
                fives_needed = change // 5
                if bank[5] >= fives_needed:
                    bank[5] -= fives_needed
                    change -= 5 * fives_needed
            
            if change != 0:
                return False
                
        return True