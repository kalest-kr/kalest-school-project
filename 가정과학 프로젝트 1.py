import matplotlib.pyplot as plt

# 데이터
categories = ['tv', 'radio', 'news', 'pc', 'notebook', 'tablet', 'smartphone']
values = [22.7, 0, 0.4, 19.7, 21.8, 20, 97.1]

# 막대 그래프 생성
plt.bar(categories, values)

# 제목과 레이블 설정
plt.title('20')
plt.xlabel('Categories')
plt.ylabel('Values')

# 그래프 표시
plt.show()
