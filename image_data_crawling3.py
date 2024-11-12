import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from urllib.request import urlretrieve
import urllib.request
import urllib
import time

url = 'https://www.google.com/search?sca_esv=cbc386de4b870031&q=%EA%B0%95%EC%95%84%EC%A7%80&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ9zKNKSjpwusJM2dYWg4btGKvTs8msUkFt41RLL2EsYFXj1HJ-6Tz3zY-OaA8p5OIwKXtepe1nwMbiobd8aopYI3Djq-_wHNSyqi1J5rXtrZ-dEOjuJfkJpxXj8pUC3HmGzP_4yQ_xdzK9qDO3vbGQ9OKpWceCh1Pu2_RMxyWEg0WL5jtkA&sa=X&ved=2ahUKEwjxz-jJgqCHAxVBrlYBHQEeD0YQtKgLegQIDRAB&biw=1707&bih=880&dpr=1.5'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
print("")

data = soup.find_all('img')
print(data)

image_list = []

# 이미지를 저장할 디렉토리 설정
os.makedirs('images', exist_ok=True)

# 이미지 다운로드 및 저장
for img in data:
    img_url = img.get('DS1iW > src')
    if not img_url:
        continue
    image_data1 = img['DS1iW > src']
    image_list.append(image_data1)

file_no = 0

for i in range(0, len(image_list)):

    try:
        urllib.request.urlretrieve(image_list[i], str(file_no) + '.jpg')
    except:
        continue

    file_no += 1
    time.sleep(0.5)


