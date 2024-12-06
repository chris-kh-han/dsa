from collections import defaultdict
import heapq


def topKFrequent(nums: list[int], k: int) -> list[int]:
    heap = []
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num, freq in freq.items():
        heapq.heappush(heap, (-freq, num))

    output = []

    for i in range(k):
        output.append(heapq.heappop(heap)[1])

    return output


topKFrequent([1, 2, 2, 3, 3, 3, 3], 2)

# 1. I prefer using a heap when I need to find k frequent elements or k largest/smallest numbers
# 2. Put minus sign before pushing into heap to ensure most frequent elements get smallest values
# 3. Then, since we need to return k most frequent elements, use a for loop with heappop
# 4. Since most frequent elements comes first as smallest in heap, we can get the right result


def topKFrequent2(nums: list[int], k: int) -> list[int]:
    nums_map = defaultdict(int)

    for num in nums:
        nums_map[num] += 1

    max_freq = max(nums_map.values())

    buckets = [[] for _ in range(max_freq+1)]

    for num, freq in nums_map.items():
        buckets[freq].append(num)

    res = []

    for freq in range(max_freq, 0, -1):
        for num in buckets[freq]:
            res.append(num)
            if len(res) == k:
                return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent2(nums, k))


# 1. I prefer using a bucket when I need to find k frequent elements or k largest/smallest numbers
# 2. Create a dictionary to store frequency of each element
# 3. Find the maximum frequency
# 4. Create a bucket with max_freq+1 elements
# 5. Iterate through the dictionary and append elements to the bucket based on their frequency
# 6. Iterate through the bucket from max_freq to 0 and append elements to result
# 7. Return result when length of result equals k
# 8. This is a more optimized solution than using a heap
# 9. Since we are using a bucket, we can achieve O(n) time complexity, Space complexity is O(n) as well
# 10. The heap solution has O(nlogn) time complexity
# 11. The heap solution is more suitable for online data streaming
# 12. The bucket solution is more suitable for offline data processing
# 13. The heap solution is more suitable for when k is much smaller than n
# 14. The bucket solution is more suitable for when k is close to n
# 15. The heap solution is more suitable for when k is close to 1
