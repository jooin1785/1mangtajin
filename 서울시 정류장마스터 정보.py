# json
import requests
import json
import pandas as pd


serviceKey = '674f4e76716a6f6f35344549574c41'
startpg = 1
endpg = 1000
STTN_ID = []
STTN_NM = []
STTN_TYPE = []
STTN_번호 = []
CRDNT_X = []
CRDNT_Y = []
BUSINFO_FCLT_INSTL_YN = []
for _ in range(71):
    url = f'http://openapi.seoul.go.kr:8088/{serviceKey}/json/tbisMasterStation/{startpg}/{endpg}/'
    startpg = endpg + 1
    endpg = endpg + 1000
    response = requests.get(url)
    rjson = response.json()

    for u in rjson['tbisMasterStation']['row']:
        STTN_ID.append(u['STTN_ID'])
        STTN_NM.append(u['STTN_NM'])
        STTN_TYPE.append(u['STTN_TYPE'])
        STTN_번호.append(u['STTN_번호'])
        CRDNT_X.append(u['CRDNT_X'])
        CRDNT_Y.append(u['CRDNT_Y'])
        BUSINFO_FCLT_INSTL_YN.append(u['BUSINFO_FCLT_INSTL_YN'])

    df = pd.DataFrame({'정류장 ID': STTN_ID, '정류장 이름': STTN_NM, '정류장 타입': STTN_TYPE, '정류장 번호': STTN_번호, '위도': CRDNT_X, '경도': CRDNT_Y, '버스도착정보': BUSINFO_FCLT_INSTL_YN})
    df.to_csv('C:\\Users\\admin\\workspaces\\crawling\\test\\서울시 정류장마스터 정보.csv')
