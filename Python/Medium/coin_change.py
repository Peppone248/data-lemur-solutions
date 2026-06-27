'''
You are given an integer array coins representing coins of different denominations and an integer target_amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
Example #1

Input: coins = [2, 4, 1, 4], target_amount = 5

Output: 2

Explanation:
There are several combinations to make up the amount 5, such as:

    using five 1's (1 + 1 + 1 + 1 + 1)
    using three 1's and one 2 (1 + 1 + 1 + 2)
    using two 2's and one 1 (2 + 2 + 1)
    using one 4 and one 1 (4 + 1)

The combination that uses the fewest coins is the last one (using 4 and 1), which totals 2 coins.
'''

def coin_change(coins, target_amount):
    def min_coins(i, current_amount):
        if current_amount == target_amount:
            return 0

        if current_amount > target_amount or i == len(coins):
            return float('inf')

        # Use current coin
        choose = 1 + min_coins(i, current_amount + coins[i])

        # Skip current coin
        skip = min_coins(i + 1, current_amount)

        return min(choose, skip)

    result = min_coins(0, 0)
    return -1 if result == float('inf') else result
  
    
