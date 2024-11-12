import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
html = requests.get(url)

#페이지 정보 가져오기
soup = BeautifulSoup(html.text, 'html.parser')
print(soup)


#name of the channel
title = soup.select('h1 > a')[0].text.strip()
print(title)

#카테고리 정보 추출
category = soup.select('p.category')[1].text.strip()
print(category)


#number of subscriber, view value, amount of vidieo
subscriber = soup.select('.subscriber_cnt')[1].text
view = soup.select('.view_cnt')[1].text
video = soup.select('.video_cnt')[1].text

print(subscriber)
print(view)
print(video)


