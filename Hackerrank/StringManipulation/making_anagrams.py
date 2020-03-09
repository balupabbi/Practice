#Reference: https://www.geeksforgeeks.org/using-counter-python-find-minimum-character-removal-make-two-strings-anagram/

from collections import Counter



def anagram(a,b):
    # make dictionaries from both strings
    dict1 = Counter(a)
    dict2 = Counter(b)

    # extract keys from dict1 and dict2
    keys1 = dict1.keys()
    keys2 = dict2.keys()

    # count number of keys in both lists of keys
    count1 = len(keys1)
    count2 = len(keys2)

    # convert list of keys in set to find common keys
    set1 = set(keys1)
    commonKeys = len(set1.intersection(keys2))

    if (commonKeys == 0):
        print( count1 + count2 )
    else:
        print( (max(count1, count2)-commonKeys) )





def anagram2(a,b):

    combined = list(set(a+b))

    input1 = Counter(a)
    input2 = Counter(b)

    min_deletion = 0

    for letter in combined:
        min_deletion = abs(input1[letter]-input2[letter]) + min_deletion

    print(min_deletion)




if __name__ == '__main__':
    anagram2('showman', 'woman')
