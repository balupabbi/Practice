



if __name__ == '__main__':
    s1 = 'world'


    for i in range(len(s1)):
        for j in range(i+1,len(s1)+1):
            print(s1[i:j])
            # print(str(i) + ':' + str(j))
