class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"(":")", "{":"}", "[":"]"}

        left = 0
        right = len(s)-1

        while left < right:
            left_symbol = s[left]
            right_symbol = s[right]
            
            if pair[left_symbol] == right_symbol:
                left += 1
                right -= 1
            else:
                return False
            
        return True

s = "()[]{}"

print(Solution().isValid(s))

