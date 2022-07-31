# json

import requests
import json
import pandas as pd


serviceKey = '684f6f61546a6f6f33374b6f6c5450'
url = f'http://openapi.seoul.go.kr:8088/{serviceKey}/json/SebcCollegeInfoKor/1/64/'

NAME_KOR = []
STATE = []
ADD_KOR = []
ADD_KOR_ROAD = []
H_KOR_GU = []
H_KOR_DONG = []

response = requests.get(url)
rjson = response.json()

for i in rjson['SebcCollegeInfoKor']['row']:
    NAME_KOR.append(i['NAME_KOR'])
    STATE.append(i['STATE'])
    ADD_KOR.append(i['ADD_KOR'])
    ADD_KOR_ROAD.append(i['ADD_KOR_ROAD'])
    H_KOR_GU.append(i['H_KOR_GU'])
    H_KOR_DONG.append(i['H_KOR_DONG'])

df = pd.DataFrame({'이름': NAME_KOR, '상태': STATE, '주소': ADD_KOR, '도로명 주소': ADD_KOR_ROAD, '구': H_KOR_GU, '행정동': H_KOR_DONG})
df.to_csv('C:\\Users\\admin\\workspaces\\crawling\\test\\서울시내 대학 및 전문대학 DB.csv')



