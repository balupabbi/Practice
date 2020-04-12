

def avglength(sentence):

    words = sentence.split(" ")

    t = 0

    avg = sum(len(word) for word in words)/len(words)
    # for i, word in enumerate(words):
    #     t += len(word)

    #avg = t/len(words)

    print(avg)


if __name__ == "__main__":
    sentence = "How are you darling?"

    avglength(sentence)
