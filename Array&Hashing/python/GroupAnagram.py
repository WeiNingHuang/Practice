from collections import defaultdict

ans = {} # can replace by defaultdict, no need to care whether if key exist
strs = ["eat","tea","tan","ate","nat","bat"]

for s in strs:
    count = [0] *26 #create an a-z array
    
    for c in s:    
        count[ ord(c) - ord('a') ] += 1 #ord("a") = 79, ord("b") = 80 ... 
    
    count = tuple(count)
    
    if count not in ans:
        ans[count]
    else:
        ans[count] += 1

ans.keys