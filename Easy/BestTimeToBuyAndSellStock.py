class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cost = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < cost:
                cost = prices[i]
            elif prices[i] >= cost:
                profit = max([profit,prices[i] - cost])
        return profit
