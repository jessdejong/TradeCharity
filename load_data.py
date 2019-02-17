import csv
import news_wrapper
import pandas as pd
import pymapd
import trading

user_str = 'JBE72D0140E8E4D8791A'
password_str = 'HMRd1eirQJdWm85td82skrATdy1LFBX8duQ9CYxT'
host_str = 'use2-api.mapd.cloud'
dbname_str = 'mapd'
connection = pymapd.connect(user=user_str, password=password_str, host=host_str, dbname=dbname_str, port=443, protocol='https')

def upload(trades):
    with open('test.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        arr = trades.split("\n")
        print(arr)
        writer.writerow(["year","month","day","money"])
        for i in arr:
            if (len(i) < 2):
                continue
            i = i.split("|")
            print(i)
            i = [i[11], i[12], i[13], i[7]]
            writer.writerow(i)

    df = pd.read_csv("test.csv")
    table_name = 'table_table'
    connection.load_table(table_name, df)
