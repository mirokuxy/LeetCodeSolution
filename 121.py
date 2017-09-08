# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    if len(prices) <= 1:
      return 0

    min_price = prices[0]
    max_profit = 0

    for i in xrange(1, len(prices)):
      profit = prices[i] - min_price
      max_profit = max(max_profit, profit)
      min_price = min(min_price, prices[i])

    return max_profit