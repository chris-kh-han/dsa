class NumArray:

    def __init__(self, nums: list[int]):
        self.output = []  # prefix_sum list
        self.length = len(nums)
        sum = 0
        for num in nums:
            sum += num
            self.output.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        if left < 0 or right >= self.length or left > right:  # Edge Cases
            return None

        if left == 0:
            return self.output[right]
        else:
            # Calculate sum[left, right] using prefix_sum
            return self.output[right] - self.output[left - 1]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))


# Initialize prefix_sum list to store cumulative sums for subarray calculations
# Time Complexity: O(n) - Single pass through the array
# Space Complexity: O(n) - Storing prefix sums
