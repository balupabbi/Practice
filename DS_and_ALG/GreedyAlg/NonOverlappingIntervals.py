"""
https://leetcode.com/problems/non-overlapping-intervals/

Reference: https://www.youtube.com/watch?v=2LUQ6tBdGxo
"""


def eraseOverlappingIntervals(intervals):
    ans = 0

    if not intervals or not intervals[0]:
        return ans
    # sorting by the first element in the list
    intervals.sort(key=lambda x: x[1])  # 1 is finishing time

    end = intervals[0][0]

    for i in intervals:
        start = i[0]

        if start < end:
            ans += 1
        else:
            end = i[1]
    return ans


if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(eraseOverlappingIntervals(intervals))