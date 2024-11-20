def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    top, bot = 0, rows - 1
    row = -1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False

    l, r = 0, cols - 1
    while l <= r:
        mid = (l+r) // 2

        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1
        else:
            return True
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))

# Initialize 1. top and bot in matrix 2. left and right in row
# Use Binary Search to find the location of the target element
# Time complexity will be O(log(n) + m), where n is the number of rows and m is the length of the row
# Space complexity will be O(1)
