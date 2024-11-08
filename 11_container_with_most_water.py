def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1

    max_area = 0

    while left < right:
        max_area = max(max_area,  min(height[left], height[right]) * (right - left) )
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# 1. Use two pointer approaches to narrow down the index to find possible higher heights and find out more heights
# 2. Calculate the container area with the smaller height and the distance between two pointers
# 3. Move the pointer of smaller height inward
# 4. Repeat the process until conditions meet