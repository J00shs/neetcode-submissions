class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1 #Left = buying, Right = Selling
        maxP = 0
        while R < len(prices):
            # Check to see if we're profitable
            # First cal the profit then, compare with previous maxP with current profit. If profit > maxP then we update to the new profit
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxP = max(maxP, profit)
            else:
                L = R
            R += 1
        return maxP


                
        