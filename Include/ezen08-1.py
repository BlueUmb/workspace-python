'''
    웹 크롤링
        - 웹페이지에 있는 데이터를 요청하여 가져오는 방법 활용
        - request, bs4 라이브러리 활용
        
        - 해당 페이지의 page controller를 직접 가져옴
        - 웹 페이지 우클릭 "페이지(프레임) 소스보기"로 같은 HTML 소스를 볼수 있음.
        - 마우스 우클릭을 하면 "검사" 기능 활용
'''

import requests
import bs4

page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
print(page_url)


source = requests.get(page_url).text
source = bs4.BeautifulSoup(source)

source = source.prettify()


print(source)