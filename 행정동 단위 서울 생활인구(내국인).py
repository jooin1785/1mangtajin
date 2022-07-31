# json 완성 X
import requests
from bs4 import BeautifulSoup
import pandas as pd

serviceKey = '534958664a6a6f6f37396863554179'
url = f'http://openapi.seoul.go.kr:8088/{serviceKey}/xml/SPOP_LOCAL_RESD_DONG/1/1000'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
content = response.text
print(content)
# row항목을 모두 찾아준다.
items = soup.find_all('row')
print(items)
row_list = []
name_list = []
value_list = []

