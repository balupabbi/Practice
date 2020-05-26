


def isPalindrome(s):

    if not s:
        return True

    i = 0
    j = len(s)-1

    while i<j:

        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True


def findallPalindromes(s):

    if not s:
        return 0

    count = 0
    paln = []

    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            print(substr)

            if len(substr) > 1:
                if isPalindrome(substr):
                    count += 1
                    paln.append(substr)

    return count,paln








if __name__ == '__main__':
    s = "aabbbaa"

    print(findallPalindromes(s))