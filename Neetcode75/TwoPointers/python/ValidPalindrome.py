"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = False
        
        new_s = ''.join(c for c in s if c.isalnum()).lower()
        
        if new_s == "":
            return True
            
        left = len(new_s)-1
        right = 0
        
        while right <= left:
            if new_s[right] == new_s[left]:
                res = True
                right += 1
                left -= 1
                
            else:
                return False
            
        return res