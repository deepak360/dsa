# Maximum Subarray Sum
def max_subarray(nums):
    n = len(nums)
    maxi = float('-inf')
    sum = 0

    for i in range(n):
        sum = nums[i] + sum
        maxi = max(maxi, sum)

        if sum < 0:
            sum = 0
    return maxi

nums = [-2,1,-3,4,-1,2,1,-5,4]
res = max_subarray(nums)
print(res)

#========================== Return Array Also ==============================
def max_subarray_with_Array(nums):
    n = len(nums)
    maxi = float('-inf')
    sum = 0
    start = end = temp_start = 0

    for i in range(n):
        sum = nums[i] + sum

        if sum > maxi:
            maxi = sum
            start = temp_start
            end = i

        if sum < 0:
            sum = 0
            temp_start = i + 1
    return maxi, nums[start:end+1]

nums = [-2,1,-3,4,-1,2,1,-5,4]
res = max_subarray_with_Array(nums)
print(res)

