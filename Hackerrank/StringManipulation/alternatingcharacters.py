








def alternatingCharacters(word):

    mindeletion = 0
    previous = ''

    for current in word:

        if current == previous:
            mindeletion += 1

        previous = current

    return mindeletion






if __name__ == '__main__':

    testcases = {'AAAA':3,'BBBBB':4,'ABABABABA':0,'BABABABA':0,'AAABBB':4}

    for test in testcases:
        print(test + ':{}'.format(alternatingCharacters(test)))
