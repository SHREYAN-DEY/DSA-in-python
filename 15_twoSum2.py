# brute force solution
# def twoSum2(nums,target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if (nums[i]+nums[j] == target):
#                 return [i+1,j+1]

# optimal solution using two pointer   
def twoSum2(nums,target):
    l = 0
    r = len(nums) - 1
    while l < r:
        sum = nums[l] + nums[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l + 1, r + 1]







numbers = [1,3,4,5,7,10,11]
target = 9
print(twoSum2(numbers,target))