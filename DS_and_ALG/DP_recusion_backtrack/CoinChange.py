"""
Reference Leetcode: https://leetcode.com/problems/coin-change/
Reference Link: https://www.youtube.com/watch?v=jgiZlGzXMBw
Python Reference: https://www.youtube.com/watch?v=m2Elp9ubY3w
Reference: https://www.youtube.com/watch?v=J2eoCvk59Rc

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest
number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the
coins, return -1.


Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
"""

"""
Dynamic Programming method with matrix: https://www.youtube.com/watch?v=Y0ZqKpToTic
Example
coins = 1,5,6,8     total = 11

 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
1
5
6
8

"""


# Function to create the matrix we'll use for the optimization
def _change_matrix(coin_set, change_amount):
    matrix = [[0 for m in range(change_amount + 1)] for m in range(len(coin_set) + 1)]
    for i in range(change_amount + 1):
        matrix[0][i] = i
    return matrix

# Function we'll use to optimize the default above matrix
def change_making(coins, change):
    matrix = _change_matrix(coins, change)
    for c in range(1, len(coins) + 1):
        for r in range(1, change + 1):

            if coins[c-1] == r:
                matrix[c][r] = 1

            elif coins[c-1] > r:
                matrix[c][r] = matrix[c-1][r]

            else:
                matrix[c][r] = min(matrix[c - 1][r], 1 + matrix[c][r - coins[c - 1]])

    return matrix[-1][-1]


def minimumCoinsGreedy(coins, amount):
    """
    Returns minimum amount of coins that make up that amount
    :param coins:
    :param amount:
    :return:
    """

    #descending order
    coins.sort(reverse=True)
    #r = amount
    min_c = []
    count = 0


    for coin in coins:
        while amount >= coin:
            amount = amount - coin
            min_c.append(coin)
            count += 1

    return count


def minimumCoinDP(coins, amount):
    pass






if __name__ == "__main__":
    #coins = [1, 5, 10]
    coins = [1,10,25]
    amount = 11
    #amount = 86

    #print(minimumCoinsGreedy(coins,amount))
    print(change_making(coins, amount))