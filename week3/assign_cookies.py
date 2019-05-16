# https://leetcode.com/problems/assign-cookies/description/
from collections import defaultdict

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        satisfied = 0
        
        # Get the biggest cookie and the highest demand at the rear or the lists
        g.sort()
        s.sort()
        
        while True:
            
            try:
                # Get the highest demand and biggest cookie
                demand = g.pop()
                cookie = s.pop()
                
                if cookie >= demand:
                    # If the cookie is big enough to satisfy demand
                    satisfied += 1
                else:
                    # If the kid was not satisfied, put cookie back
                    s.append(cookie)
            except IndexError:
                # If theres no more children or cookies, break
                break
            
        
        return satisfied