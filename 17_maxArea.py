# BRUTE FORCE
def maxArea(height):
    res = 0
    for l in range(len(height)):
        for r in range( l + 1, len(height)):
            w = ((r+1)-(l+1))
            h = min(height[l], height[r])
            area = w * h
            res = max(res, area)
    return res

height = [1,7,2,5,4,7,3,6]
print(maxArea(height))






