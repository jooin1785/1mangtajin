
# json 완성
import requests
import json
from pandas.io.json import json_normalize
from sqlalchemy import create_engine
import time
import schedule
def sql():
    nowtime = time.strftime('%y%m%d%H%M')
    startpg = 1
    endpg = 1000
    rows = []
    serviceKey = '6253425a556a6f6f313137777359494e'
    for _ in range(3):
        url = f'http://openapi.seoul.go.kr:8088/{serviceKey}/json/bikeList/{startpg}/{endpg}/'
        startpg = endpg + 1
        endpg = endpg + 1000
        response = requests.get(url)
        contents = response.text
        json_ob = json.loads(contents)
        body = json_ob['rentBikeStatus']['row']
        dataframe = json_normalize(body)
        engine = create_engine("mysql+pymysql://root:1234@localhost/test")
        conn = engine.connect()
        dataframe.to_sql(name=nowtime, con=engine,
                         if_exists='append', index=False)

schedule.every(5).minutes.do(sql)

while True:
    schedule.run_pending()
    time.sleep(1)
# 데이터 값 출력
# contents = response.text
# print(contents)
#
# # 문자열을 json으로 변경
# json_ob = json.loads(contents)
# print(json_ob)
# print(type(json_ob))
#
# # 필요한 내용만 꺼내기
# body = json_ob['rentBikeStatus']['row']
# print(body)
#
# # dataframe으로 만들기
# dataframe = json_normalize(body)
# print(dataframe)
# dataframe.info()
# engine = create_engine("mysql+pymysql://root:1234@localhost/test")
# conn = engine.connect()
#
# dataframe.to_sql(name='test', con=engine,
#                  if_exists='append', index=False)
