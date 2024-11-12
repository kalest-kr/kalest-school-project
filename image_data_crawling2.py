import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import os
from urllib.request import urlretrieve
from PIL import Image
import urllib.request
import urllib
import time
from PIL import Image



url = 'https://www.google.com/search?sca_esv=cbc386de4b870031&q=%EA%B0%95%EC%95%84%EC%A7%80&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ9zKNKSjpwusJM2dYWg4btGKvTs8msUkFt41RLL2EsYFXj1HJ-6Tz3zY-OaA8p5OIwKXtepe1nwMbiobd8aopYI3Djq-_wHNSyqi1J5rXtrZ-dEOjuJfkJpxXj8pUC3HmGzP_4yQ_xdzK9qDO3vbGQ9OKpWceCh1Pu2_RMxyWEg0WL5jtkA&sa=X&ved=2ahUKEwjxz-jJgqCHAxVBrlYBHQEeD0YQtKgLegQIDRAB&biw=1707&bih=880&dpr=1.5'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
print("")

list_of_image = []

data = soup.find_all('img')

print(data)

print(type(data))

# 모든 img 태그를 찾고 src 속성 값을 추출하는 함수
def extract_src(tag_list):
    srcs = []
    for tag in tag_list:
        if tag.has_attr('src'):
            srcs.append(tag['src'])
    return srcs

# 함수 호출
src_values = extract_src(data)
print(src_values)



save_directory = "C:/Users/ginok/PycharmProjects/pythonProject/images"


# 리스트를 순회하며 각 URL에서 이미지를 다운로드
for i, url in enumerate(data):
    # 파일 이름을 URL의 마지막 부분을 사용하여 생성
    file_name = os.path.basename(url)
    # 파일 저장 경로
    save_path = os.path.join(save_directory, file_name)
    # 이미지 다운로드 함수 호출
    download_image(url, save_path)
