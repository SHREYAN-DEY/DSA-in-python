# prefix & suffix
def productExceptSelf_1(nums: list[int]):
    #calculate the length of the input array
    n = len(nums)
    # creating 3 list for storing values
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


def productExceptSelf_2(nums):
    # the array that we wil fill w the values
        answer = [1] * len(nums)

        # calculate up until i 
        prefix = 1
        for i in range(len(nums)):
            # if not curr idex num, we multply it 
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        # calculate up until i R to L
        # iterate backwards through the array
        for i in range(len(nums) - 1, -1, -1):
            # if not curr idex num, we multply it 
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer


nums = [1,2,3,4]
# nums = [-1,0,1,2,3]
res = productExceptSelf_2(nums)
print(res)
