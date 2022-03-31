class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # two pointer to specific the date
        l_pointer, r_pointer = 0, 1 # buy date < sell date
        # temp max value
        maxP = 0

        while r_pointer < len(prices):
            # profitable?
            if prices[l_pointer] < prices[r_pointer]: # profit
                profit = prices[r_pointer] - prices[l_pointer]
                maxP = max(maxP, profit) # update the max value
            else:
                l_pointer = r_pointer # since right pointer price is lower (better to buy)
            
            r_pointer += 1
        return maxP

        