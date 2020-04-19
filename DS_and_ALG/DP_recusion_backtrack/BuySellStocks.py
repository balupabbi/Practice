"""
Buy Sell stocks: https://www.youtube.com/watch?v=mj7N8pLCJ6w
Buy Sell stockII: https://www.youtube.com/watch?v=blUwDD6JYaE
"""

def maxProfit(s):
    """
    O(n^2) solution for only one transaction
    :param s:
    :return:
    """

    #Brute Force

    p = 0
    days = []

    for i in range(len(s)):
        for j in range(i,len(s)):
            diff = s[j]-s[i]

            if diff > p:
                p = diff
                days = [i,j]

    return p, days


def maxProfit2(prices):
    """
    O(n) solution where theres is only one transaction
    :param s:
    :return:
    """

    if not prices:
        return 0

    max_profit = float("-inf") #profit
    min = float("inf")



    for i in range(len(prices)):

        if prices[i] < min:
            min = prices[i]

        max_profit = max(max_profit,prices[i]-min)

    return max_profit


def buysell2(prices):
    """
    Multiple transactions for max profit
    :param prices:
    :return:
    """

    mp = 0 #sum(cmax-cmin)

    if not prices:
        return mp


    for i in range(len(prices)-1):

        if prices[i]<prices[i+1]:
            cp = prices[i+1] - prices[i]
            mp += cp


    return mp



if __name__ == "__main__":
    s = [7,1,5,3,4,6]
    #s = []
    #s= [7,6,4,3,1]
    #s = [2,4,1]

    #print(maxProfit2(s))
    print(buysell2(s))
