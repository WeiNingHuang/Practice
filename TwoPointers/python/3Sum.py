nums = [-1,0,1,2,-1,-4]

l = 0
r = len(nums)-1

res = []
while(l < r):
    pre = nums[l]
    post = nums[r]
    cur = nums[l] + nums[r]
    dif = 0 - cur

    for i,n in enumerate(nums[l+1:r]):
        if (n == dif):
            res.append([n,pre,post])
    r -=1
        


            

