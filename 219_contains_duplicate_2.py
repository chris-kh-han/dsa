def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window = {}
    L = 0

    for R in range(len(nums)):
        window[nums[R]] = window.get(nums[R], 0) + 1

        if window[nums[R]] == 2:
            return True

        if R - L + 1 > k:
            window[nums[L]] -= 1
            L += 1

    return False

# Initialize a dictionary 'window' to keep track of the counts of elements and 'L' as the left index of the window.
# Iterate through the list 'nums' with 'R' as the right index.
# Increment the count of the current element in the 'window'. If the count becomes 2, return True.
# If the size of the window exceeds 'k', decrement the count of the element at the left index and move 'L' to the right.
# Time complexity is O(n) where n is the length of the 'nums' array, and space complexity is O(k) where k is the size of the window.
