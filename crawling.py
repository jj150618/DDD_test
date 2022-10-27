from dotenv import load_dotenv
import os

import requests
import pandas as pd
import time

while 1:
    try:
        year = input("Please enter the year : ")
        if 1987 <= int(year) <= 2020:
            break
        else:
            print("Please enter from 2007 to 2010.")
    except ValueError:
        print("Please enter the format of the year only.")


load_dotenv()
auth_key = os.environ.get('AUTH_KEY')

dt_index = pd.date_range(start=year+'0101', end=year+'1231')
dt_list = dt_index.strftime("%Y%m%d").tolist()

total_df = pd.DataFrame()

for i in dt_list:
    url = f'http://openAPI.seoul.go.kr:8088/{auth_key}/json/DailyAverageCityAir/1/25/{i}'
    try:
        response = requests.get(url).json()
        temp_df = pd.DataFrame(response['DailyAverageCityAir']['row'])
        total_df = pd.concat([total_df, temp_df])
        print(i)
        if int(i) % 10 ==0:
            time.sleep(1)
    except:
        pass

total_df.to_csv("./src/data/dust_"+year+".csv")
