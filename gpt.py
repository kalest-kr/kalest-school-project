from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
data = requests.get(url)

#페이지 정보 가져오기
soup = BeautifulSoup(data.text, 'html.parser')

print(soup)

#카테고리 정보 추출
category = soup.select('p.category')[0].text.strip
print(category)

#name of the channel
title = soup.select('h1 > a')[0].text.strip()
print(title)

#number of subscriber, view value, amount of vidieo
subscriber = soup.select('.subscriber_cnt')[1].text
view = soup.select('.view_cnt')[1].text
video = soup.select('.video_cnt')[1].text

#반복문으로 채널 정보 추출하기
channel_list = soup.select('tbody > tr')

i = 0

for channel in channel_list:
    title = channel.select('h1 > a')[0].text.strip()
    category = channel.select('p.category')[0].text.strip()
    subscriber = channel.select('.subscriber_cnt')[0].text
    view = channel.select('.view_cnt')[0].text
    video = channel.select('.video_cnt')[0].text

    print(title, category, subscriber, view, video)
    i += 1

    if i == len(channel_list) - 1:
        break

#data save
results = []

#씨이ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ발

for page in range(1, 11):
    url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}"
    data = requests.get(url)

    # 페이지 정보 가져오기
    soup = BeautifulSoup(data.text, 'html.parser')

    channel_list = soup.select('form > table > tbody > tr')
    for channel in channel_list:
        title = channel.select('h1 > a')[0].text.strip()
        category = channel.select('p.category')[0].text.strip()
        subscriber = channel.select('.subscriber_cnt')[0].text
        view = channel.select('.view_cnt')[0].text
        video = channel.select('.video_cnt')[0].text
        data = [title, category, subscriber, view, video]
        print(data)
        results.append(data)


