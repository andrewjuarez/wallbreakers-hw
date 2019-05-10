# https://leetcode.com/problems/word-pattern/submissions/

class Solution:
    def wordPattern(self, pattern: str, str1: str) -> bool:
        mapping = {}
        
        words = str1.split(" ")
        
        if len(words) != len(pattern):
            return False;
        
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != words[i]:
                    return False
            elif words[i] in mapping.values():
                return False
            else:
                mapping[pattern[i]] = words[i]
        
        return True
            
        