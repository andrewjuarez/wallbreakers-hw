# https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s) / 2)):
            char = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = char
        
                     