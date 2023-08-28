"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede
"""
##

class Solution():
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i', 'o', 'u']

        left = 0
        right = len(s)-1

        while left <= right:
            if s[left] in vowels:
                if s[right] in vowels:
                    temp = s[left]
                    s = s[:left] + s[right] + s[left+1:]
                    s = s[:right] + temp + s[right+1:]

                    right -= 1
                elif s[right] not in vowels:
                    right -= 1
            else:
                left += 1
            
        return s
    

s = Solution()

a = s.reverseVowels("leetcode")

print(a)