





def reverseInt(x):
    if not x:
        return x

    ans = ''

    while x != 0:

        d = abs(x) % 10
        if x < 0:
            ans = "-" + str(d)
        else:
            ans += str(d)

        x = int(abs(x)/10)

    return int(ans)





if __name__ == "__main__":
    i = -123

    print(reverseInt(i))