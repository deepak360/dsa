"""Write a Python program that finds all unique pairs of numbers in a list that add up to a specific target sum. The program should take a list and a target sum as input and output a list of unique pairs.
Example Input:
input_list = [1, 3, 2, 2, 4, 0, 5, -1]
target_sum = 4
Expected Output:
pairs = [(1, 3), (2, 2), (5, -1),(4,0)]
 """
 

def unique_pair(nums, target):
    sort_num = sorted(nums)
    i = 0
    j = len(sort_num) - 1
    result = []

    while i < j:
        current_sum = sort_num[i] + sort_num[j]

        if current_sum == target:
            result.append((sort_num[i], sort_num[j]))
            i += 1
            j -= 1

            while i < j and sort_num[i] == sort_num[i - 1]:
                i += 1
            while i < j and sort_num[j] == sort_num[j + 1]:
                j -= 1

        elif current_sum < target:
            i += 1
        else:
            j -= 1

    return result


input_list = [1, 3, 2, 2, 4, 0, 5, -1]
target = 4
result = unique_pair(input_list, target)
print(result)      
# Output: [(-1, 5), (0, 4), (1, 3), (2, 2)]

