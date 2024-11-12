from bs4 import BeautifulSoup
import requests

# 웹 페이지 URL
url = 'https://www.google.com/search?sca_esv=cbc386de4b870031&q=%EA%B0%95%EC%95%84%EC%A7%80&udm=2&fbs=AEQNm0DmKhoYsBCHazhZSCWuALW8l8eUs1i3TeMYPF4tXSfZ9zKNKSjpwusJM2dYWg4btGKvTs8msUkFt41RLL2EsYFXj1HJ-6Tz3zY-OaA8p5OIwKXtepe1nwMbiobd8aopYI3Djq-_wHNSyqi1J5rXtrZ-dEOjuJfkJpxXj8pUC3HmGzP_4yQ_xdzK9qDO3vbGQ9OKpWceCh1Pu2_RMxyWEg0WL5jtkA&sa=X&ved=2ahUKEwjxz-jJgqCHAxVBrlYBHQEeD0YQtKgLegQIDRAB&biw=1707&bih=880&dpr=1.5'

# requests를 사용하여 HTML 가져오기
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)
