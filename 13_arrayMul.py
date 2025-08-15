# prefix & suffix
def productExceptSelf(nums: list[int]):
    n = len(nums)
    res = [0] * n
    prefix = [0] * n
    suffix = [0] * n
    
    prefix[0] = suffix[n - 1] = 1
    for i in range(1,n):
        prefix[i] = nums[i-1] * prefix[i-1]
    
    for i in range(n-2, -1, -1):
        suffix[i] = nums[i+1] * suffix[i+1]
    print(prefix)
    
    for i in range(0,n):
        res[i] = prefix[i] * suffix[i]
    print(suffix)

    return res


nums = [1,2,3,4]
# nums = [-1,0,1,2,3]
res = productExceptSelf(nums)
print(res)
