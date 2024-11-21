def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort()
    res = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prev_end:  # intervals are sorted ascending order already, so we don't have to check prev_start
            prev_end = end
        else:
            res += 1
            prev_end = min(prev_end, end)
            # keep the interval with the smallest to maximize future spaces

    return res


print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))


# Time complexity will be O(nlogn) because of sorting
# Space complexity will be O(1)
