"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/

"""


def merge_sorted(n1,n2):
    #loop backwards
    i = 0
    for e in n1:
        if e !=0:
            i+=1
    i = i-1
    j = len(n2)-1

    for k in reversed(range(len(n1))):

        if i < 0 or j < 0:
            break
            
        if n1[i] > n2[j]:
            n1[k] = n1[i]
            i -= 1
        elif n1[i] <= n2[j]:
            n1[k] = n2[j]
            j -= 1


    return n1




if __name__ == "__main__":
    n1 = [1,3,5,0,0,0]
    n2 = [2,4,6]

    print(merge_sorted(n1,n2))