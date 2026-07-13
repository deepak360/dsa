def unique_pair(input_list, target):
    input_list = sorted(input_list)
    i = 0
    n = len(input_list)
    j = n-1
    result = []
    while i < j:
        curr_sum  = input_list[i] + input_list[j]
        if curr_sum == target:
            result.append((input_list[i], input_list[j]))
            i+=1
            j-=1
            while i < j and input_list[i] == input_list[i-1]:
                i+=1
            while i < j and input_list[j] == input_list[j+1]:
                j-=1
        else:
            if curr_sum < target:
                i+=1
            else:
                j-=1
    return result

input_list = [1, 3, 2, 2, 4, 0, 5, -1]
target = 4
result = unique_pair(input_list, target)
print(result)