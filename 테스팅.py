from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests


browser = webdriver.Chrome('C:\chromedriver-win64\chromedriver.exe')
url = "https://youtube-rank.com/board/bbs/tag_board.php?bo_table=youtube_video&q=%EB%A8%B9%EB%B0%A9"
browser.get(url)

#페이지 정보 가져오기
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

head_line = soup.select('.media-heading')[0].text.strip()
channel = soup.select('.media-info > a')[0].text.strip()
video_info = soup.select(".media-info")[0].text.strip()

response = requests.get(url)

print(response.text)
print(head_line)
print()
print(channel, video_info)
