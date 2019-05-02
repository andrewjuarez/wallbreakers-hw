# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            #print("iterating", num)
            possible = num
            while num > 1:
                #print("num:", num)
                digit = num % 10
                if digit == 0:
                    break
                if possible % digit != 0:
                    break
                num = int(num / 10)
            #print("out of while loop, num:", num)
            if num <= 1:
                result.append(possible)
        return result