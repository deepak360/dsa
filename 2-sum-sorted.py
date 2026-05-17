"""
Pair Sum - Sorted
Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].

"""

def TwoSum(nums, target):
    n = len(nums)
    seen = {}
    for i in range(n):
        if target - nums[i] not in seen:
            seen[nums[i]] = i
        else:
            return [seen[target-nums[i]], i]
            
# nums, target = [-5, -2, 3, 4, 6], 7 
nums, target = [1, 1, 1], 2
result = TwoSum(nums, target)
print(result)