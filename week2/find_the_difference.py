# https://leetcode.com/problems/find-the-difference/
from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictS = defaultdict(int)
        dictT = defaultdict(int)
        
        for char in s:
            dictS[char] += 1
        
        for char in t:
            if char not in dictS:
                return char
            else:
                dictT[char] += 1
        
        for char in dictS:
            if dictS[char] != dictT[char]:
                return char