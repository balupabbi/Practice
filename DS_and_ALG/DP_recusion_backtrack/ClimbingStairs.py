"""
Leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
Youtube: https://www.youtube.com/watch?v=uHAToNgAPaM
BacktoBack SWE: https://www.youtube.com/watch?v=NFJ3m9a1oJQ

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

"""




"""
n  #of ways (1step or 2steps)
0  1
1  1
2  1w+2w = 1,1 | 2 = 2ways
3  2w+1w = 1,1,1 | 2,1 | 1,2 = 3ways
4  3w+1w = 1,1,1,1 | 1,2,1 | 2,1,1 | 1,1,2 |2,2 = 5ways
5  8ways
"""




def climbStairsTD(n,memo):
    """
    O(2^n) recursive approach
    but through meoization becomes O(n) time complexity and space complexity
    :param n:
    :return:
    """
    #st = {}
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if memo[n]>0:
            return memo[n]
        else:
            memo[n] = climbStairsTD(n-1,memo) + climbStairsTD(n-2,memo)
            return memo[n]



def climbStairsBU(n):
    """
    O(n) time complexity
    O(n) space complexity
    bottom up approach
    :return:
    """

    dp = [0 for i in range(n+1)] #index n --> 0 ... n [0,1,2,]
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]








if __name__ == "__main__":
    n = 10

    print(climbStairsBU(n))

    memo = [0 for i in range(n+1)]
    print(climbStairsTD(n,memo))