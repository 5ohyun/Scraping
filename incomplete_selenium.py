import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium import webdriver as wd

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.implicitly_wait(10)

driver.get('https://pedia.watcha.com/ko-KR/decks/OphYTWVoSDLG')

response = requests.get('https://pedia.watcha.com/ko-KR/decks/OphYTWVoSDLG')
soup = BeautifulSoup(response.text, 'html.parser')
movies_list = soup.select('ul.css-xv4sal-VisualUl-ContentGrid-DeckContentGrid.e12idbfv16 > li')
print(movies_list)

final_movie_data = []

for movie in movies_list:
        a_tag = movie.select_one('a')

        movie_title = a_tag['title']
        movie_code = a_tag['href'].split('contents/')[1]

        movie_data = {
            'title': movie_title,
            'code': movie_code,
        }
        final_movie_data.append(movie_data)

        print(final_movie_data)

SCROLL_PAUSE_TIME = 10

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
# 화면 최하단으로 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 페이지 로드를 기다림
    time.sleep(SCROLL_PAUSE_TIME)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 새로운 높이가 이전 높이와 변하지 않았을 경우 스크롤 종료
    if new_height == last_height:
        break

    # 스크롤 다운이 된다면 스크롤 다운이 된 후의 창 높이를 새로운 높이로 갱신
    last_height = new_height






# with open('./brand_infos.csv', mode='w') as brand_infos:
#     brand_writer = csv.writer(brand_infos)

#     for list in brand_list:
#         brand_writer.writerow([list["name"], list["img"], list["link"]])


# for movie in final_movie_data:
#     movie_code = movie['code']

#     # 영화 리뷰의 경우 headers 체크를 따로 하지 않아서 굳이 보낼 필요 없음
#     params = (
#         ('code', movie_code),
#         ('type', 'after'),
#         ('isActualPointWriteExecute', 'false'),
#         ('isMileageSubscriptionAlready', 'false'),
#         ('isMileageSubscriptionReject', 'false'),
#     )

#     response = requests.get(
#         'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', params=params)

#     soup = BeautifulSoup(response.text, 'html.parser')

#     review_list = soup.select('body > div > div > div.score_result > ul > li')

#     count = 0

#     for review in review_list:
#         score = review.select_one('div.star_score > em').text
#         reple = ''

#         # 일반적인 경우 먼저 처리 (일반적인 것을 먼저 처리하는 것이 효율적이다)
#         if review.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count}') is None:
#             reple = review.select_one(
#                 f'div.score_reple > p > span#_filtered_ment_{count}').text.strip()
#         # 리뷰가 긴 경우 처리
#         elif review.select_one(f'div.score_reple > p > span#_filtered_ment_{count} > span#_unfold_ment{count}'):
#             reple = review.select_one(
#                 f'div.score_reple > p > span#_filtered_ment_{count} > span > a')['data-src']

#         print(score, reple)

#         count += 1
