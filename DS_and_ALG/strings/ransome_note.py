





def checkMagazine(magazine,note):
    words_mag = magazine.split(' ')
    words_note = note.split(' ')
    word_dic = {}

    for word in words_mag:
        if word not in word_dic:
            word_dic[word]=1
        else:
            word_dic[word]= word_dic[word] + 1

    for word in words_note:
        if word in word_dic:
            word_dic[word]=word_dic[word]-1
            if word_dic[word] < 0:
                #means more replicated words in note so return NO
                return "NO"
        else:
            return "NO"

    return "YES"


if __name__ == '__main__':
    magazine = "two times three is not four"
    note = "two times two is four"

    print (checkMagazine(magazine,note))