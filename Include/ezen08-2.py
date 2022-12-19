# ezen08-2
'''
    * 웹 크롤링
        - 웹 페이지에 있는 데이터를 요청하여 가져오는 방법 활용
        - request, bs4(BeautifulSoup) 라이브러리 활용
            - BeautifulSoup4(bs4)
                - HTML source에서 tag별 계층 구조를 파악하기 쉽게 parse tree 형태로 변환해주는 라이브러리
                - 손쉽게 HTML source에서 원하는 정보를 추출할 수 있음
                    - find(), fina_all() 함수를 이용하면 원하는 tag와 속성에 맞는 모든 정보를 가져올 수 있음

        - 해당 페이지의 page source를 직접 가져옴
        - 웹 페이지 우클릭 "페이지(프레임) 소스보기"로 같은 HTML 소스를 볼수 있음
        - 마우스 우클릭을 하면 "검사" 기능 활용
'''


page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
print(page_url)

import requests
import bs4

source = requests.get(page_url).text

source = bs4.BeautifulSoup(source)
dates = source.find_all('td', class_ = 'date')

date_list = []
for date in dates:
    date_list.append(date.text)
print(date_list)
print(f"date_list 개수 : {len(date_list)}개")

#체결가 추출
prices = source.find_all('td', class_ = 'number_1')

price_list = []
for price in prices[::4]:
    price_list.append(price.text)
print(price_list)
print(f"price_list개수 : {len(price_list)}개")


last_url = source.find_all('td', class_ = 'pgRR')[0].find_all("a")[0]['href']
max_page_no = int(last_url.split('=')[-1])
