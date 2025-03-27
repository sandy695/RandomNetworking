'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

class Solution:
    def maxProfit(self, prices):
        min = prices[0]
        max = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < max:
                profit = profit + (max - min)
                min = prices[i]
                max = prices[i]
            if prices[i] > max:
                max = prices[i]
        profit = profit + (max - min)
        return profit

# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Peak Valley Approach, greedy algorithm
'''
A Greedy Algorithm makes locally optimal choices at each step to reach a globally optimal solution. 
It works well for problems that have an optimal substructure, meaning that solving smaller subproblems optimally leads to the best overall solution.
'''

# Test cases
s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 7
print(s.maxProfit([1, 2, 3, 4, 5]))  # Output: 4
print(s.maxProfit([7,6,4,3,1])) # 0
                
                
