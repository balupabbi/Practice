"""
Python Questions -
1) Print Max element of a given list
2) Print median of a given list
3) Print the first nonrecurring element in a list
4) Print the most recurring element in a list
5) Greatest common Factor
6) Find the mismatching words between 2 strings


"""

from collections import defaultdict, OrderedDict

def gcf(a,b):
    """

    :param a:
    :param b:
    :return:
    """
    i = 1
    ans = None

    while i <= min(a,b):
        if a % i == 0 and b % i == 0:

            if ans != None:
                if ans < i:
                    ans = i
            else:
                ans = i

            i += 1
        else:
            i+=1


    return ans


def validateIP(ip):
    """
    valid IP: xxx.xxx.xxx.xxx, where xxx is a number from 0-255
    :param ip:
    :return:
    """
    if not ip:
        return False

    chunks = ip.split('.')
    check = []

    if len(chunks) == 4:
        for p in chunks:
            if not int(p) >= 0 and int(p) <= 255:
                return False
            else:
                check.append(True)
    else:
        return False

    if all(check) == True:
        return True

def removedup(a):
    """

    :param a:
    :return:
    """
    if not a:
        return None

    a1 = {}

    if a is list:
        return list(set(a))
    elif isinstance(a,str):
        for l in a:
            if l in a1:
                a1[l] +=1
            else:
                a1[l] = 1

        res = ""

        #res = "".join(x for x in sorted(a1.keys()))

        for k, v in a1.items():
            res = res + k

        return res


def stringmismatch(a1, a2, method):
    """

    :param a1:
    :param a2:
    :return:
    """

    #Hashing
    #Use a hash table of size 26 for all the lowercase characters.
    #Initially, mark presence of each character as ‘0’ (denoting that the character is not present in both the strings).
    #Traverse the 1st string and mark presence of each character of 1st string as ‘1’ (denoting 1st string) in the hash table.
    #Now, traverse the 2nd string. For each character of 2nd string, check whether its presence in the hash table is ‘1’ or not.
    # If it is ‘1’, then mark its presence as ‘-1’ (denoting that the character is common to both the strings), else mark its
    # presence as ‘2’ (denoting 2nd string).



    if method == "Hashmap":

        #a1 = str(set(a1))
        #a2 = str(set(a2))


        u = defaultdict(int) #k=letter, value=(int)

        for s in a1:
            u[s] = 1

        for s in a2:
            if s in a1:
                u[s] -= 1
            else:
                u[s] = 1

        #value is 0 then its common, else if >=1 then unique
        res = []
        for k,v in u.items():
            if v == 1:
                res.append(k)

        return res

    #Brute force method

    elif method == "BruteForce":
        if not a1 or not a1:
            return "Not Valid"

        unique = []

        a1 = list(set(a1)) # get all unique letters
        a2 = list(set(a2))

        for l in a1:
            if l not in unique and l not in a2:
                unique.append(l)

        for l in a2:
            if l not in unique and l not in a1:
                unique.append(l)

        return unique



def most_recurring(a):
    """

    :param a:
    :return:
    """
    wc = {}

    for i, e in enumerate(a):
        if e not in wc.keys():
            wc[e] += 1

    most = 0
    for key, value in wc.items():
        if value > most:
            most = value

    for key, value in wc.items():
        if value == most:
            return key


def first_nonrecurring(a):
    a = 'RRRGGGUUULLLUMNY'

    wc = {}

    for i,c in enumerate(a,start=1):
        if a[i] != a[i-1]:
            return a[i]

    return

def median(a):

    a = sorted(a)

    # 0,1,2,3 = even, mid = 4/2 = 2
    # 0,1,2 = odd, mid = 3/2 = 1.5 -> 1

    if len(a) % 2 == 0:
        #Even
        mid = len(a)/2
        median = (a[mid] + a[mid-1])/2
    else:
        #Odd
        mid = len(a)/2
        media = a[mid]

    return median

def maxElem(a):

    return max(a)

    a = sorted(a)
    res = a[-1]


if __name__ == "__main__":
    a = [9,3,45,6]

    a1 = '..'  #l, o, v, b
    a2 = 'babae'

    ip = '-1.34.201.76'

    print(gcf(100,20))
    #print(stringmismatch(a1,a2,'Hashmap'))

    #print(removedup(a1))

    #print(validateIP(ip))
    #Hash map l, o, v  --> missing b, a