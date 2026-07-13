"""
Container With Most Water
Given an array height, where each element represents the height of a vertical line, 
find two lines that together with the x-axis form a container that holds the
maximum amount of water.

Example
height = [1,8,6,2,5,4,8,3,7]

Output = 49
"""

def max_water(height):
    n = len(height)
    left = 0
    right = n-1

    maxi = float('-inf')
    while left < right:
        area = (right - left) * min(height[left], height[right])
        maxi = max(maxi, area)
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
        
    return maxi

height = [1,8,6,2,5,4,8,3,7]
res = max_water(height)
print(f"The maximum amount of water that can be held is {res}")