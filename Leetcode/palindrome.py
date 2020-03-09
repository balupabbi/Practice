#Alpha numeric: https://www.quora.com/What-is-a-non-alpha-numeric-character

def isPalindrome(s):
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





if __name__ == "__main__":

    valid = "A man, a plan, a canal: Panama"
    valid2 = "racecar"
    not_valid = "racecarand"

    if isPalindrome(valid):
        print("Above string is a palindrome")
    else:
        print("Not a palindrome")

    if isPalindrome(valid2):
        print("Above string is a palindrome")
    else:
        print("Not a palindrome")

    if isPalindrome(not_valid):
        print("Above string is a palindrome")
    else:
        print("Not a palindrome")


