# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrences = {}
        for i in range(len(s)):
            if s[i] in occurrences:
                occurrences[s[i]][0] += 1
            else:
                occurrences[s[i]] = [1, i]
        
        index = len(s)
        for char in occurrences:
            if occurrences[char][0] == 1:
                if index > occurrences[char][1]:
                    index = occurrences[char][1]
        
        if index == len(s):
            return -1
        else:
            return index