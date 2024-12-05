def findBuildings(heights: list[int]) -> list[int]:
    stack = []

    for i in range(len(heights)):
        while stack and heights[i] >= heights[stack[-1]]:
            stack.pop()

        stack.append(i)

    return stack


print(findBuildings([4, 2, 3, 1]))


# Time: O(n)
# Space: O(n)

# Given a list of building heights, return the indices of the buildings
# that have an ocean view. A building has an ocean view if it is taller
# than all the buildings to its right.
