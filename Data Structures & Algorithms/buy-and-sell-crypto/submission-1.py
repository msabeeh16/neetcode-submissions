class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(i, len(prices)):
                sell_price = prices[j]
                curr_profit = sell_price - buy_price
                profits.append(curr_profit)
        return max(profits)

