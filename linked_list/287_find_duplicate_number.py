from collections import defaultdict


def findDuplicate(nums: list[int]) -> int:
    num_dict = defaultdict(int)

    for num in nums:
        num_dict[num] += 1
        if num_dict[num] == 2:
            return num


print(findDuplicate([1, 3, 4, 2, 2]))

# Initialize a dictionary 'num_dict' to keep track of the counts of elements.
# Iterate through the 'nums' list.
# For each element, increment its count in 'num_dict'.
# If the count of any element reaches 2, return that element as the duplicate.
# Time complexity: O(n), where n is the size of 'nums'.
# Space complexity: O(n), where n is the size of 'nums' (due to the dictionary).
