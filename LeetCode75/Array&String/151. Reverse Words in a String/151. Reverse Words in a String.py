"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string."""
##
class Solution:
    def reverseWords(self, s: str) -> str:
        s_lst = s.split(" ")

        start = 0
        end = len(s_lst)-1

        while start <= end:
            if s_lst[start] != " ":
                if s_lst[end] != " ":
                    s_lst[start], s_lst[end] = s_lst[end], s_lst[start]

                    start += 1
                    end -= 1
                elif s_lst[end] == " ":
                    end -= 1

            else:
                start += 1

        new_s = ' '.join(i for i in s_lst if i != "")

        return new_s

    
##
s = "  hello    world  "
s_lst = s.split(" ")

new_s = ""
for i in s_lst:
    if i != "":
        new_s = new_s.join(i)