"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true"""
##
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        
        for i, v in enumerate(s):
            if v not in dict_1:
                dict_1[v] = [i]
            else:
                dict_1[v].append(i)

        for i, v in enumerate(t):
            if v not in dict_2:
                dict_2[v] = [i]
            else:
                dict_2[v].append(i)
            
        # if dict_1.values() == dict_2.values():
        values = zip(dict_1.values(), dict_2.values())

        for value in values:
            if value[0] != value[1]:
                return False
        
        return True

##

s = 'paper'
t = 'title'
a = Solution()
res = a.isIsomorphic(s, t)

print(res)