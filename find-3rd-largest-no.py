"""Find 3rd Largest number in an unsorted array
arr = [5,2,8,7,10,12,9]
"""
import heapq

def thirdLargest(nums, k):
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap,nums[i])
        if i >=k:
            print(i, heap)
            heapq.heappop(heap)
    
    return heap[0]

arr = [5,2,8,7,10,12,9]
k=3
result = thirdLargest(arr, k)
print(f'Your 3rd largest number is {result}')