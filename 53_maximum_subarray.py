def maxSubArray(nums: list[int]) -> int:
    max_sum = float('-inf')
    cur_sum = 0

    for num in nums:
        cur_sum += num
        max_sum = max(cur_sum, max_sum)

        if cur_sum < 0:
            cur_sum = 0

    return max_sum


# Set max_sum to the most negative value so the first value in the sequence will replace max_sum.
# While cur_sum is positive, there is a possibility it will become the maximum number followed by a positive number.
# If cur_sum < 0, we need to reset the sequence, so reset it to 0.
# Space and time complexity will be O(n), where n stands for the size of the nums array, and O(1) as it only uses constant space.
