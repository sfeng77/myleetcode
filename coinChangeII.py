#  You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
#
# Note: You can assume that
#
#     0 <= amount <= 5000
#     1 <= coin <= 5000
#     the number of coins is less than 500
#     the answer is guaranteed to fit into signed 32-bit integer
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        nc = len(coins)
        coins.sort(reverse = True)
        if nc == 0:
            if amount ==0:
                return 1
            else:
                return 0
        dp = {}

        def findChange(amount, n):
            if n == 1:
                if coins[-1] == 0:
                    if amount == 0:
                        return 1
                    else:
                        return 0
                if amount % coins[-1] == 0:
                    return 1
                else:
                    return 0

            if (amount, n) not in dp:
                count = 0
                c = coins[nc - n]
                for i in range(amount/c + 1):
                    count += findChange(amount - c * i, n  - 1)
                dp[(amount, n)] = count

            return dp[(amount, n)]

        return findChange(amount, nc)
