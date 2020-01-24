import pandas as pd




def initialize_dates():
    data={'product':['lee','lha','lhc','lxj','vl6','vl8'], 'enddt':['20190902','20190902','20190902','20190831','20190902','20190902']}
    df = pd.DataFrame(data)
    df.to_csv('latest_dates.csv')
    #df = pd.read_csv('latest_dates.csv', delimiter=',')

def read_dates(product):
    """
    Only run if the current - stored date = 2 and update stored date the date that you just ran
    :return:
    """
    latest_lee = '20190902'

    df = pd.read_csv('latest_dates.csv')
    res = df.loc[df['product'] == product]
    store_enddt = str(res['enddt'][0])
    print (store_enddt)

    if latest_lee - store_enddt == 2:
        print("Run with store_enddt +1")
        #Store the enddt
    else:
        print("Don't run")





if __name__ == "__main__":
    product = 'lee'
    read_dates(product)

    #print(res)