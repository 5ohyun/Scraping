import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium import webdriver as wd
import pandas as pd
import numpy as np


watcha_ratings = pd.read_csv('C:/Users/leeso/Downloads/김준태/movie/result/watcha_ratings.csv', names = ['userId','movieId','rating','timestamp'])
watcha_movie_id=pd.unique(watcha_ratings['movieId'])
movie_result = []

watcha_movie_id


for i in watcha_movie_id :
    response = requests.get('https://pedia.watcha.com/ko-KR/contents/'+i+'/overview')
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select_one('dd.css-11yx0y9-DescriptionDetail.e1kvv3953').get_text()
    item_list = soup.find_all("dd", class_ = "css-11yx0y9-DescriptionDetail e1kvv3953")

    try :
        genres = item_list[3].get_text() # 에러가 발생할 가능성이 있는 코드

    except IndexError :  # 에러 종류
        genres = np.nan # 에러가 발생 했을 경우 처리할 코드

        
    print([i, title, genres])
    movie_result.append([i, title, genres])

        
final_movie_data=pd.DataFrame(movie_result, columns = ['movieId','title','genres'])
final_movie_data.to_csv('movies_append_list.csv',index=False)