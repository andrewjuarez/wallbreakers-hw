// https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i = 0
            j = len(row) - 1
            
            while i <= j:
                temp = row[i]
                row[i] = row[j] ^ 1
                row[j] = temp ^ 1
                
                i = i + 1
                j = j - 1
        return image