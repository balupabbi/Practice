


"""
hello

    oellh

    olleh


    string[::-1]
"""




def reverseSentence(s):

    if not s or len(s)<2:
        return s

    words = s.split(' ')

    i = 0
    j = len(words) -1

    while i < j:
        tmp = words[i]
        words[i] = words[j]
        words[j] = tmp

        i += 1
        j -= 1

    for i,w in enumerate(words):
        words[i] = w[::-1]


    return words




if __name__ == '__main__':
    s = "Hello World is easy"

    print(reverseSentence(s))