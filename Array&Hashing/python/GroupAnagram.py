from collections import defaultdict
#%%
ans = {} # can replace by defaultdict, no need to care whether if key exist

strs = ["eat","tea","tan","ate","nat","bat"]

for s in strs:
    count = [0] *26 #create an a-z array
    
    for c in s:    
        count[ ord(c) - ord('a') ] += 1 #ord("a") = 79, ord("b") = 80 ... 
    
    if tuple(count) not in ans:
        ans[tuple(count)] = [s]
    else:
        ans[tuple(count)].append(s)


#%%
# use defaultdict
ans = defaultdict(list) # can replace by defaultdict, no need to care whether if key exist

strs = ["eat","tea","tan","ate","nat","bat"]

for s in strs:
    count = [0] *26 #create an a-z array
    
    for c in s:    
        count[ ord(c) - ord('a') ] += 1 #ord("a") = 79, ord("b") = 80 ... 
    
    ans[count].append(s)