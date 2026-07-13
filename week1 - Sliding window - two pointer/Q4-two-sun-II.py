"""
Two Sum II
Given a sorted array numbers and a target, 
return the 1-based indices of the two numbers that add up to the target.
"""

def two_sum_II(nums, target):
    n = len(nums)
    left = 0
    right = n-1

    while left < right:
        sum = nums[left] + nums[right]
       
        if sum == target:
            return [left+1,right+1]
        elif sum > target:
            right-=1
        elif sum < target:
            left+=1





numbers = [2,7,11,15] 
target = 9

res = two_sum_II(numbers, target)
print(f"The indices of the two numbers that add up to {res}")