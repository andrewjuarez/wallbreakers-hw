# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        positions = []
        
        s = list(s)
        
        for i in range(len(s)):
            if s[i].lower() in ('a', 'o', 'u', 'i', 'e'):
                vowels.append(s[i])
                positions.append(i)
        
        vowels = vowels[::-1]
        for i in range(len(vowels)):
            s[positions[i]] = vowels[i]
        
        return "".join(s)