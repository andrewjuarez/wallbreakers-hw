# https://leetcode.com/problems/uncommon-words-from-two-sentences/submissions/

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:        
        word_listA = set()
        word_listB = set()
        
        multiple_A = set()
        multiple_B = set()
        for item in A.split(" "):
            if item not in word_listA:
                word_listA.add(item)
            else:
                multiple_A.add(item)
        
        for item in B.split(" "):
            if item not in word_listB:
                word_listB.add(item)
            else:
                multiple_B.add(item)
        
        for item in multiple_A:
            word_listA.remove(item)
            if item in word_listB:
                word_listB.remove(item)
                if item in multiple_B:
                    multiple_B.remove(item)
            
        for item in multiple_B:
            word_listB.remove(item)
            if item in word_listA:
                word_listA.remove(item)
                if item in multiple_A:
                    multiple_A.remove(item)
        
        uncommon = []
        
        for item in word_listA:
            if item not in word_listB:
                uncommon.append(item)
                
        for item in word_listB:
            if item not in word_listA:
                uncommon.append(item)
                
        return uncommon