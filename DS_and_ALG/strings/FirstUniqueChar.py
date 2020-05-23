
def firstUniqChar(s: str) -> int:

    u = set(s)
    f = u.pop()

    for i in range(len(s)):
        if s[i] == f:
            return i





if __name__ == "__main__":
    s = "leetcode"
    print(firstUniqChar(s))