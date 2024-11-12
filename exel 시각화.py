import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('youtube_rank.xlsx')
df.head()

##숫자 정리
df['replaced_subscriber'] = df['subscriber'].str.replace('만', '000')

#데이터 타입 변환
df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')

#카테고리별 구독자수, 채널수 정리
pivot_df = df.pivot_table(index='category', values='replaced_subscriber', aggfunc=['sum', 'count'])

#데이터 프레임의 칼럼명 변경
pivot_df.columns = ['subscriber_sum', 'category_sum']

##데이터 프레임의 인덱스 초기화
pivot_df = pivot_df.reset_index()

#데이터 내림차순 정렬
pivot_df = pivot_df.sort_values(by='subscriber_sum', ascending=False)

#value of subscribers of each category
plt.figure(figsize=(30, 10))
plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()

#value of channels for each category
pivot_df = pivot_df.sort_values(by='category_sum', ascending=False)

plt.figure(figsize=(30, 10))
plt.pie(pivot_df['category_sum'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()
