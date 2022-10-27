from services.predict_dust.domain.predict_dust_service import MakeInputExecutor
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta


class MakeInputExecutorImpl(MakeInputExecutor):
    def __init__(self,) -> None:
        super().__init__()

    def _get_api_response(self, date: str):
        load_dotenv()
        auth_key = os.environ.get('AUTH_KEY')
        url = f'http://openAPI.seoul.go.kr:8088/{auth_key}/json/DailyAverageCityAir/1/25/{date}'
        response = requests.get(url)
        return response

    def make_input_array(self, date: str, region: str):
        today_date = datetime.strptime(date, '%Y%m%d')
        yesterday_date = (today_date + relativedelta(days=-1)).strftime("%Y%m%d")
        last_month_date = (today_date  + relativedelta(months=-2)).strftime("%Y%m%d")

        dt_index = pd.date_range(start=last_month_date, end=yesterday_date)

        dt_list = dt_index.strftime("%Y%m%d").tolist()

        dust_list = list()
        for day in dt_list:
            try:
                response = self._get_api_response(day).json()
                for i in response['DailyAverageCityAir']['row']:
                    if i['MSRSTE_NM'] == region:
                        dust_list.append(i['PM10'])
                        break
            except:
                pass

        input_array = [dust_list[-15:]]
        return input_array
