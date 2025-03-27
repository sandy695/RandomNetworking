'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
'''

class Solution:
    def canCompleteCircuit(self, gas, cost):
        # check if the sum of gas is less than the sum of cost
        if sum(gas) < sum(cost):
            return -1
        # initialize variables
        start = 0
        tank = 0
        # iterate through the list
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # if the tank is less than 0, update the start index and reset the tank
            if tank < 0:
                start = i + 1
                tank = 0
        return start

# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Greedy algorithm

# Test cases
s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3

class Solution1:
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        current_tank = 0
        starting_station = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            
            if current_tank < 0:
                starting_station = i + 1
                current_tank = 0
        
        return starting_station if total_tank >= 0 else -1

# Time complexity: O(n)
# Space complexity: O(1)
# What algorithm is used ? Greedy algorithm

# Test cases
s1 = Solution1()
print(s1.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # Output: 3
print(s1.canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # Output: -1