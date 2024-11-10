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
