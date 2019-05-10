# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set()
        for jewel in J:
            jewels.add(jewel)
        
        count = 0
        for stone in S:
            if stone in jewels:
                count += 1
        
        return count
                