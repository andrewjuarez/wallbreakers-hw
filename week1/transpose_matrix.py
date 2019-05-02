# https://leetcode.com/problems/transpose-matrix/description/

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(A[0])):
            result.append([])
        for row_index in range(len(A)):
            for col_index in range(len(A[row_index])):
                result[col_index].append(A[row_index][col_index])
        return result
                