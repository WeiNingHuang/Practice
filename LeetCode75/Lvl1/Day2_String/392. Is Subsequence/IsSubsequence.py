"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false"""
##

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
       
        for i in t:
            cur = s[left:]  
            if len(cur) == 0:
                return True
            
            if i == cur[0]:
                left += 1

        if len(cur) == 0:
            return True        
        else:
            return False



##
s = 'c'
t = 'abc'

a = Solution()
a.isSubsequence(s, t)


