# json 완성
import requests
import pandas as pd

serviceKey = '7564614f626a6f6f3532656e426643'

STATN_ID = []
STATN_NM = []
ROUTE = []
CRDNT_X = []
CRDNT_Y = []

url = f'http://openapi.seoul.go.kr:8088/{serviceKey}/json/subwayStationMaster/1/764/'
response = requests.get(url)
rjson = response.json()
for u in rjson['subwayStationMaster']['row']:
    STATN_ID.append(u['STATN_ID'])
    STATN_NM.append(u['STATN_NM'])
    ROUTE.append(u['ROUTE'])
    CRDNT_X.append(u['CRDNT_X'])
    CRDNT_Y.append(u['CRDNT_Y'])

    df = pd.DataFrame({'역사_ID': STATN_ID, '역사명': STATN_NM, '호선': ROUTE, '위도': CRDNT_X, '경도': CRDNT_Y})
    df.to_csv('C:\\Users\\admin\\workspaces\\crawling\\test\\서울시 역사마스터 정보')
