def findBuildings(heights: list[int]) -> list[int]:
    stack = []

    for i in range(len(heights)):
        while stack and heights[i] >= heights[stack[-1]]:
            stack.pop()
        stack.append(i)

    return stack


print(findBuildings([4, 2, 3, 1]))

# Loop through the heights and check if the current height is greater than and equal to the height at the top of the stack.
# If it is, pop the stack until the current height is less than the height at the top of the stack.
# Append the current height to the stack.
# Return the stack.
# Time complexity: O(n)
# Space complexity: O(n)
