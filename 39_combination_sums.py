def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(i, curr, currentSum):
        if i >= len(candidates) or currentSum > target:
            return None
        if currentSum == target:
            res.append(curr.copy())
            return

        curr.append(candidates[i])
        dfs(i, curr, currentSum + candidates[i])
        curr.pop()
        dfs(i+1, curr, currentSum)

    dfs(0, [], 0)

    return res


print(combinationSum([2, 3, 6, 7], 7))
