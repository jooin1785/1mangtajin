# xml형식 크롤링

import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

serviceKey = '41476252676a6f6f33305749506e59'
url = f'http://openapi.seoul.go.kr:8088/{serviceKey}/xml/LOCALDATA_082501/1/1000/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
content = response.text

# row항목을 모두 찾아준다.
items = soup.find_all('row')
row_list = []
name_list = []
value_list = []
for i in range(0, len(items)):
    columns = items[i].find_all()
    #첫째 행 데이터 수집
    for j in range(0,len(columns)):
        if i ==0:
            # 컬럼 이름 값 저장
            name_list.append(columns[j].name)
        # 컬럼의 각 데이터 값 저장
        value_list.append(columns[j].text)
    # 각 행의 value값 전체 저장
    row_list.append(value_list)
    # 데이터 리스트 값 초기화
    value_list=[]

big_store_df = pd.DataFrame(row_list, columns=name_list)
engine = create_engine("mysql+pymysql://root:1234@localhost/test")
conn = engine.connect()

big_store_df.to_sql(name='big_store', con=engine,
                 if_exists='replace', index=False)