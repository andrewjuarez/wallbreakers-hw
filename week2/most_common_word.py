# https://leetcode.com/problems/most-common-word/description/
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set()
        for word in banned:
            banned_set.add(word.lower())
            
            
        words = paragraph.replace(", ", " ").replace(",", " ").replace("; ", " ").replace(";", " ").split(" ")
        
        word_count = defaultdict(int)
        for word in words:
            word = word.lower().strip("!?.;',")
            if word not in banned_set:
                word_count[word] += 1
        
        most_common_word = ""
        most_common_count = 0
        
        for word, count in word_count.items():
            if count > most_common_count:
                most_common_count = count
                most_common_word = word
        
        return most_common_word
            