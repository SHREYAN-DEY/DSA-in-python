def threeSum(nums):
    res = []
    nums.sort()
    
    for i, n in enumerate(nums):
        if i > 0 and n == nums[i-1]:
            continue
        
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum = n + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res
                



# nums = [-3,3,4,-3,1,2]
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))