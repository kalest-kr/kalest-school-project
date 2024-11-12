import requests
from bs4 import BeautifulSoup
import os
import re

def download_image(url, save_path):
    try:
        # 이미지 데이터를 가져옴
        response = requests.get(url)
        response.raise_for_status()  # 요청이 성공했는지 확인

        # 이미지를 바이너리 쓰기 모드로 파일에 저장
        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Image successfully downloaded: {save_path}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def clean_filename(filename):
    # 파일 시스템에서 사용할 수 없는 문자를 제거하고 유효한 파일 이름으로 변경
    cleaned_filename = re.sub(r'[<>:"/\\|?*]', '', filename + '.jpg')
    return cleaned_filename

# 웹 페이지 URL
url = 'https://www.google.com/search?sca_esv=cbc386de4b870031&q=%EA%B0%95%EC%95%84%EC%A7%80&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ9zKNKSjpwusJM2dYWg4btGKvTs8msUkFt41RLL2EsYFXj1HJ-6Tz3zY-OaA8p5OIwKXtepe1nwMbiobd8aopYI3Djq-_wHNSyqi1J5rXtrZ-dEOjuJfkJpxXj8pUC3HmGzP_4yQ_xdzK9qDO3vbGQ9OKpWceCh1Pu2_RMxyWEg0WL5jtkA&sa=X&ved=2ahUKEwjxz-jJgqCHAxVBrlYBHQEeD0YQtKgLegQIDRAB&biw=1707&bih=880&dpr=1.5'

# requests를 사용하여 HTML 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 img 태그를 찾고 src 속성 값을 추출
image_tags = soup.find_all('img')
image_urls = [img['src'] for img in image_tags if img.has_attr('src')]

# 이미지를 저장할 디렉토리 생성
save_directory = "C:/Users/ginok/PycharmProjects/pythonProject/강아지"
os.makedirs(save_directory, exist_ok=True)

# 각 이미지를 다운로드하여 저장
for i, url in enumerate(image_urls):
    try:
        # 파일 이름 추출
        filename = os.path.basename(url)
        cleaned_filename = clean_filename(filename)
        # 저장할 경로 설정
        save_path = os.path.join(save_directory, cleaned_filename)
        # 이미지 다운로드 함수 호출
        download_image(url, save_path)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# 웹 페이지 URL
url = 'https://www.google.com/search?sca_esv=e58adf53c043c182&q=%EA%B3%A0%EC%96%91%EC%9D%B4&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ9zKNKSjpwusJM2dYWg4btGKvTs8msUkFt41RLL2EsYFXj1HJ-6Tz3zY-OaA8p5OIwLlYAhqYgKeQsybVCfK3TClp5eJ8pKyvjHPuKkxzOkfs39PPooyb18QionBChgkg3bORCI0L1Q6BO3S5b3bJfdHG6epm&sa=X&ved=2ahUKEwib5cPdg62HAxV2YvUHHUtiHnYQtKgLegQIEBAB&biw=1707&bih=880&dpr=1.5'

# requests를 사용하여 HTML 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 모든 img 태그를 찾고 src 속성 값을 추출
image_tags = soup.find_all('img')
image_urls = [img['src'] for img in image_tags if img.has_attr('src')]

# 이미지를 저장할 디렉토리 생성
save_directory = "C:/Users/ginok/PycharmProjects/pythonProject/고양이"
os.makedirs(save_directory, exist_ok=True)

# 각 이미지를 다운로드하여 저장
for i, url in enumerate(image_urls):
    try:
        # 파일 이름 추출
        filename = os.path.basename(url)
        cleaned_filename = clean_filename(filename)
        # 저장할 경로 설정
        save_path = os.path.join(save_directory, cleaned_filename)
        # 이미지 다운로드 함수 호출
        download_image(url, save_path)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

