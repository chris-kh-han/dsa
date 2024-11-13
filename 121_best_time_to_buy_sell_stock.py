def maxProfit(prices: list[int]) -> int:
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r  # Move the buy day to the current sell day if a lower price is found
        r += 1  # Move the sell day to the next day
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))


# Initialize buy day l and sell day r
# Use two pointers to find the maximum profit, where prices[r] should be greater than prices[l]
# Compare current profit with max_profit to track the highest possible profit
# space O(1) time O(n)
