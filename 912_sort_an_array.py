def sortArray(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    m = len(nums) // 2

    left = sortArray(nums[:m])
    right = sortArray(nums[m:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])


print(sortArray([5, 2, 3, 1]))  # [1, 2, 3, 5]

# Split the array at the midpoint and recursively sort until len(nums) <= 1
# Then merge and compare each element of the subarrays
# Time complexity: O(n log n), where n is the size of the array. The merge sort algorithm recursively splits the array into two halves until each subarray contains a single element. This splitting process takes O(log n) time, where n is the size of the array. Merging two sorted subarrays takes O(n) time.
# Space complexity: O(n) for the result, the recursion stack space is O(log n), but this is dominated by the O(n) space required for the result array.
