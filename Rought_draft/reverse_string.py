


def reverse(x):
    result = ''
    for i in x:
        result = i + result
        print (result)

    return result




if __name__ == "__main__":
    res = reverse("hello")

    print(res)