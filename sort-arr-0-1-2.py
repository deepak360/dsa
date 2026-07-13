"""
Sort an array of 0,1,2
"""

def sort_array(arr):
    n = len(arr)
    low = mid = 0
    high= n-1

    while(mid <= high): #low < high
        if arr[mid]==0:
            arr[low],arr[mid] = arr[mid], arr[low]
            low+=1
        elif arr[mid] == 1:
            mid +=1
        else:
            arr[mid], arr[high] =  arr[high], arr[mid]
            high -=1
    return arr

arr = [2,1,2,1,2,1,0,1,0,0,1,1,2]
res = sort_array(arr)
print(res)