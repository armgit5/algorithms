# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://www.geeksforgeeks.org/stock-buy-sell/

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1183350/Python-Easy-solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_profit = max(profit, max_profit)

        return max_profit

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
assert s.maxProfit(prices) == 5

prices = [7,6,4,3,1]
print(s.maxProfit(prices))
assert s.maxProfit(prices) == 0
