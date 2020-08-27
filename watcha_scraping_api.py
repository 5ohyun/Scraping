import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


movie_list=[]

for i in range(1,42) :
    for a in range(12) : 
        headers = {
            'authority': 'api-pedia.watcha.com',
            'x-watcha-client-version': '2.0.0',
            'accept': 'application/vnd.frograms+json;version=20',
            'x-watcha-client-language': 'ko',
            'x-watcha-client': 'watcha-WebApp',
            'x-watcha-remote-addr': '220.95.42.18',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'x-watcha-client-region': 'KR',
            'origin': 'https://pedia.watcha.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://pedia.watcha.com/ko-KR/decks/OphYTWVoSDLG',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_gid=GA1.2.1288284538.1598411359; _c_drh=true; _gat=1; _ga=GA1.1.1510708654.1598411359; _ga_1PYHGTCRYW=GS1.1.1598453956.6.1.1598453957.0; _guinness_session=HTmyiVNRKA2%2F4ggJ9JeptWwQLTgSL0g%2F6HLRsr6UEr0Q34dqFuqllW%2FJ6SN%2FQCT%2Bgq%2F71bDA8kpJrqJAEVOZ1L7j--03K55p6s1bYAvYNc--XIK3xUCJNScVHNniJ9t46w%3D%3D',
            'if-none-match': 'W/"6123abad4d557be0c59df942d6345d8c"',
        }

        params = (
                ('page', i),
                ('size', '12'),
        )

        response = requests.get('https://api-pedia.watcha.com/api/decks/OphYTWVoSDLG/items', headers=headers, params=params)

        #NB. Original query string below. It seems impossible to parse and
        #reproduce query strings 100% accurately so the one below is given
        #in case the reproduced version is not "correct".
        # response = requests.get('https://api-pedia.watcha.com/api/decks/OphYTWVoSDLG/items?page=5&size=12', headers=headers)


        result_dict = json.loads(response.text)
        movieid = result_dict['result']['result'][a]['content']['code'] #[19]['user']
        title= result_dict['result']['result'][a]['content']['title']
        genres= result_dict['result']['result'][a]['content']['genres']
        movie_list.append([movieid, title, genres])
    
    print(movie_list)



#print(movie_list)

movie=pd.DataFrame(movie_list,columns=['movieid', 'title', 'genres'])

movie.to_csv('watcha_movie_list.csv',encoding='euc-kr',index=False)




