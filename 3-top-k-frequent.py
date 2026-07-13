##  Top K Frequent Elements - Problem: [1,1,1,2,2,3], k=2 → [1,2]
"""
We have to find the k=2 most frequent element in the array
Time: O(n log n)  Space: O(n)
"""
##  Approach1 - sort by frequency


def top_k_frequent(nums, k):
    from collections import Counter
    count = Counter(nums)
    print(count)
    return [x for x, _ in count.most_common(k)]


nums= [1,1,1,2,2,3]
k=2
result = top_k_frequent(nums, k)
print(result)

##  Approach2 (Optimized): heap + Bucket Sort