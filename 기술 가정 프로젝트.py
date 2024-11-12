from selenium import webdriver
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome('C:\chromedriver-win64')
url = "https://www.mediastat.or.kr/statHtml/statHtml.do?orgId=005&tblId=DT_164002_B024&vw_cd=undefined&list_id=undefined&scrId=&seqNo=&language=ko&obj_var_id=undefined&itm_id=undefined&conn_path=I2&path="
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

response = requests.get(url)

print(response)