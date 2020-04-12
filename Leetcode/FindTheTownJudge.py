
"""
Reference: https://www.youtube.com/watch?v=kxSc4-EWO1A
"""

def findTownJudge(N,trust):
    counts = [None]+ [0]*N

    for val in trust:
        counts[val[1]] += 1
        counts[val[0]] -= 1

    #Everyone trusts judge so count of judge = N-1

    for i, c in enumerate(counts):
        if c == (N-1):
            return i

    return -1



if __name__ == '__main__':
    N = 4
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    print (findTownJudge(N,trust))