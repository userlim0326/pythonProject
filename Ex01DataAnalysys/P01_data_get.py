# raise Exception('강제 예외 발생')
# raise ValueError
error_message = """Traceback (most recent call last):
  File "C:\\workspace\\PycharmProjects\\pythonProject\\Ex01DataAnalysys\\P01_data_get.py", line 1, in <module>
    raise Exception('강제 예외 발생')
Exception: 강제 예외 발생
"""
# 파이썬의 기본 문법들을 활용하여 텍스트 데이터 내에서 불필요한 데이터를 제고하거나
# 패턴을 찾아 필요한 데이터만 분리하는 등의 데이터 분석을 진행하기 위함.

error_date = "[2024-04-11 14:00:00]"
print(error_message)
# f = open('2024-04-11_error_log.txt', 'w', encoding='utf8')
with open('2024-04-11_error_log.txt', 'w', encoding='utf8') as f:
  print(error_message, error_date , file=f)
f.close()

f = open('2024-04-11_error_log.txt', 'r', encoding='utf8')
data = f.read()
print(data)
f.close()

f = open('data.csv', 'r', encoding='utf8')
data = f.read()
print(data)
f.close()

import csv
f = open('data.csv', 'r', encoding='utf8')
data = csv.reader(f)
print(type(data))
for i in data:
  print(i)

import json
a = [1,2,3,{'4':5, '6':7}]
b = json.dumps(a) # 파이썬 객체 -> JSON 변환
print(b)
c = json.loads(b) # JSON -> 파이썬 객체 변환
print(c)

from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen('https://news.naver.com/section/105')
bs = BeautifulSoup(html.read(), 'html.parser')

# 1) css selector를 활용
titles = bs.select('.ct_scroll_wrapper>div>div>ul>li>a')
titles = bs.select('.as_headline>.sa_list>._SECTION_HEADLINE>.sa_item_inner>.sa_item_flex>.sa_text>.sa_text_title>strong')
print(len(titles))
for i in range(len(titles)):
    print(i+1, titles[i].text)

# find 찾으면 첫번째 꺼, find_all 복수개를 들고 옴
# first = bs.find('div', class_="as_section_headline").find('div', class_='as_headline').find('ul', class_='sa_list')
# lis = first.find_all('li', class_="_SECTION_HEADLINE")
# for s in lis:
#   temp = str(s.find('strong', class_="sa_text_strong"))
#   start = temp.find('">')+2
#   end = temp.find("</")
#   print(temp[start:end])
