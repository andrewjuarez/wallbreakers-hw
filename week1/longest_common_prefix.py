# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        index = 0
        prefix = ""
        current = ""
        
        while True:
            try:
                if index >= len(strs[0]):
                    raise Exception
                current = strs[0][index]
                #print('current:', current)
                for word in strs:
                    #print('word:', word)
                    #print('checking:', word[index], "against", current)
                    if word[index] != current:
                        raise Exception
                prefix += current
                index += 1
                
            except Exception:
                break
        
        return prefix
            