##
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_s = ""
        word1_p = 0
        word2_p = 0
        len_word1 = len(word1)
        len_word2 = len(word2)

        while True:
            if word1_p < len_word1 and word2_p < len_word2:
                new_s += word1[word1_p]
                new_s += word2[word2_p]
                word1_p += 1
                word2_p += 1
            
            elif word1_p == len_word1 and word2_p < len_word2:
                new_s += word2[word2_p]
                word2_p += 1

            elif word2_p == len_word2 and word1_p < len_word1:
                new_s += word1[word1_p]
                word1_p += 1

            else:
                break

        return new_s
        
##

a = 'abc'
b = 'qwertasdf'

s = Solution()
s.mergeAlternately(a,b)


##
