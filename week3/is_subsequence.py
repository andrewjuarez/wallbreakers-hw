# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        
        try:
            index = 0
            for char in t:
                if char == s[index]:
                    index +=1
                    if(index == len(s)):
                        return True
        except IndexError:
            # If we check the entire s substring we know it is a substring
            return True
        
        # If we manage to pass through all of t we know s is not a substring
        return False