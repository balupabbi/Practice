from collections import OrderedDict, Counter

MAX_CHAR = 26

def issubstring(s1,s2):

    a = set(s1)
    b = set(s2)

    if a.intersection(b):
        return 'YES'
    else:
        return 'NO'


def issubstring_mysolution(s1,s2):
    store = OrderedDict()

    for i in s1:
        if i not in store:
            store[i] = 1
        else:
            store[i] = store[i]+1

    for j in s2:
        if j in store:
            store[j] = store[j]-1

    substring=''

    for k,v in store.items():
        if v == 0:
            substring = substring + k

    if substring:
        return 'YES'
    else:
        return 'NO'

def isAnagram(s1,s2):
    """
    https://www.asciitable.xyz/python-program-convert-string-character-to-ascii-code/
    ab is anagram of ba
    :return:
    """

    if len(s1) != len(s2):
        return 'Not Anagram'
    elif not s1 and not s2:
        return 'Not Anagram'

    arr = [0]*256

    if not s1 and not s2:
        return

    #Change all to lower case
    s1 = s1.lower()
    s2 = s2.lower()

    for i in s1:
        arr[ord(i)] += 1

    for i in s2:
        arr[ord(i)] -= 1

    if all(i == 0 for i in arr ):
        return 'Anagram'
    else:
        return 'Not Anagram'


def sortString(s):

    return ''.join(sorted(s))


def sortString2(str):
    # Hash array to keep count of characters.
    # Initially count of all charters is
    # initialized to zero.
    charCount = [0 for i in range(MAX_CHAR)]

    # Traverse string and increment
    # count of characters
    for i in range(0, len(str), 1):
        # 'a'-'a' will be 0, 'b'-'a' will be 1,
        # so for location of character in count
        # array we wil do str[i]-'a'.
        charCount[ord(str[i]) - ord('a')] += 1

    # Traverse the hash array and print
    # characters
    for i in range(0, MAX_CHAR, 1):
        for j in range(0, charCount[i], 1):
            print(chr(ord('a') + i), end="")


def lengthOfLongestSubstring(s):
    def hasDuplicates(s1):
        r1 = set(s1)

        if len(s1) != len(r1):
            return True
        else:
            return False

    """
       #lets print all possible substrings
       # Works only if its not case sensitive
       #lets only look at lowercase
       #a-z 26 finite array,
       :param s: 
       :return: 
       """
    s = s.lower()

    result = 0

    for i in range(len(s)):
        for (j) in range(len(s)):
            #check if substring has duplicates, if it does
            #print(s[i:j+1])
            if hasDuplicates(s[i:j+1]):
                continue
            else:
                result = max(result,len(s[i:j+1]))

    return result


def lenghtOfLongestSubstring2(s):
    """
    Using sliding window
    :param s:
    :return:
    """

    return

def removeDuplicates(s):
    """

    :param s:
    :return:
    """
    if not s:
        return "Empty String"

    result = ''

    for i in s:
        if i in result:
            continue
        else:
            result += i

    return result
    # for i in range(len(s)):
    #     for j in range(i+1,len(s)):
    #         print(s[i:j])

def removeDuplicatesInPlace(nums):
    """
    takes in array
    :param arr:
    :return:
    """

    x = 1
    for i in range(len(nums) - 1):
        if (nums[i] != nums[i + 1]):
            nums[x] = nums[i + 1]
            x += 1
    return (x)
    # x = 0
    #
    # for i in range(1,len(arr)):
    #     if arr[x] != arr[i]:
    #         x+=1
    #         arr[x] = arr[i]
    #     else:
    #         continue
    #
    # return arr[0:(x+1)]


def isPalindrome(s):
    # Alpha numeric: https://www.quora.com/What-is-a-non-alpha-numeric-character
    print(s)
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True


if __name__ == '__main__':
    s1 = 'hellue'
    s2 = 'world'

    arr = [0,0,1,1,1,2,2,3,3,4]

    print(removeDuplicatesInPlace(arr))
    # print(issubstring(s1,s2))
    #print(isAnagram(s1,s2))
    #lengthOfLongestSubstring(s2)
    # print(lengthOfLongestSubstring(s2))