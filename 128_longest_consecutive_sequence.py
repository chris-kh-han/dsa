def longestConsecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    longest = 0
    for i in range(len(nums)):
        length = 1
        if nums[i] - 1 not in nums_set:
            while nums[i] + length in nums_set:
                length += 1

        longest = max(longest, length)

        return longest


print(longestConsecutive([2, 20, 4, 10, 3, 4, 5]))


# Create a variable nums_set to remove any duplicate elements in the nums list
# Initialize length as 1 since every element will have a length of 1 if there are no consecutive numbers
# Check if nums[i] - 1 is not in nums_set, which means it could be the starting point of a sequence
# Loop until nums[i] is no longer consecutive
# Return the length of the longest consecutive sequence
