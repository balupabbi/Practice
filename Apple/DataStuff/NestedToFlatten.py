"""
https://www.geeksforgeeks.org/python-convert-nested-dictionary-into-flattened-dictionary/

Given a nested dictionary, the task is to convert this dictionary into a flattened
dictionary where the key is separated by ‘_’ in case of the nested key to be started.
"""


def helper(nd,out):

    for k,v in nd.items():

        if isinstance(v,dict):
            out = helper(v,out)
        else:
            out.append(v)

    return out

def nested_to_list(nd):

    out = []

    for k, v in nd.items():
        item = []
        item.append(k)
        if isinstance(v,dict):
            item = helper(v,item)

        out.append(item)


    return out



def flattenNaive(nd,separator):


    out = {}
    for k, v in nd.items():
        if isinstance(v,dict):

            res = flattenNaive(v,separator)

            for k2, v2 in res.items():
                inside_key = k2
                value = v2
                out[k + separator + inside_key] = value

        else:
            out[k] = v


    return out









if __name__ == '__main__':
    input = {'geeks': {'Geeks': {'for': 7}}, 'Geeks': {'for': {'geeks': 4, 'for': 1}}, 'for': {'geeks': {'Geeks': 3}}}
    print(flattenNaive(input, separator='_'))

    # nd = {
    #     1: {'header':'H1', 'body': 'B1', 'footer': 'F1'},
    #     2: {'header':'H2', 'body': 'B2', 'table': {'r1':'100','r2':'200','r3':{'rr1':'1000'}}, 'footer': 'F2'}
    # }
    #
    # print(nested_to_list(nd))
    #print(output)
