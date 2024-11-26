def minCostClimbingStairs(cost: list[int]) -> int:
    memo = {}

    def helper(k):
        if k >= len(cost):
            return 0
        if k in memo:
            return memo[k]

        memo[k] = cost[k] + min(helper(k+1), helper(k+2))
        return memo[k]

    return min(helper(0), helper(1))


print(minCostClimbingStairs([10, 15, 20]))


# The minimum cost to reach the top from step k is the cost at step k plus the minimum
# cost of reaching the top from step k+1 or step k+2.
# Memoization is utilized to store and reuse the results of subproblems, enhancing efficiency.
# Space Complexity: O(n) due to the memoization dictionary.
# Time Complexity: O(n) because each step is computed only once.
