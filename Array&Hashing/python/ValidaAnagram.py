class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s)!= len(t):
            return False
        
        hash_map = {}
        
        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        for j in t:
            if j in hash_map:
                hash_map[j] -= 1

        for k in hash_map:
            if hash_map[k] != 0:
                return False

        return True

a = Solution()

s = "a"
t = "nagaram"
print(a.isAnagram(s, t))

s = {'a':0, 'b':5, 'c':6}

s.get('a',3)

