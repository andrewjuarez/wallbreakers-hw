# https://leetcode.com/problems/detect-capital/description/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            # Entire word is uppercase
            return True
        elif word[0].upper() == word[0] and word[1:] == word[1:].lower():
            # Only the first letter is uppercase
            return True
        elif word == word.lower():
            # All letters in word are lowercase
            return True
        return False
        