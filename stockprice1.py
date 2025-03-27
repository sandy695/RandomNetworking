'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''

class Solution:
    def maxProfit(self, prices):
        min = prices[0]
        max = prices[0]
        max_profit = 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < min:
                min = prices[i]
                max = prices[i]
            if prices[i] > max:
                max = prices[i]
                profit = max - min
            if profit > max_profit:
                max_profit = profit
        return max_profit

# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Peak Valley Approach, greedy algorithm

# Test cases
s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 5
print(s.maxProfit([7,6,4,3,1])) # 0

        