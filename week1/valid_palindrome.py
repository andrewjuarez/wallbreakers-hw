# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for char in s:
            if s.isalnum():
                check += s
    
        right = len(check)
        print(check)
        for left in range(len(check) // 2):        
            print("checking", check[left], "and", check[right])
            if check[left].lower() != check[right].lower():
                return False
            right -= 1
        
        return True