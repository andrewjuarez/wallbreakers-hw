# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        s = ""
        for i in range(len(words)):
            s += words[i][::-1] + " "
        return s[:-1]
        