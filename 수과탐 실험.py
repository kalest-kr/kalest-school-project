import numpy as np
import pandas as pd
from scipy import integrate

# 장축의 절반의 길이
a = 10

# 초점의 거리
c = 0

# 둘레 값
length = 0

# 세타 분모
m = 0

# 세타 값
ceta = np.radians(m)

# 데이터 값 저장
list1 = []
list2 = []
list3 = []

# 타원의 둘레 계산
while c < a:
    k = c / a  # 이심률
    length = lambda theta: np.sqrt(1 - ((k ** 2) * (np.cos(theta) ** 2)))
    perimeter, _ = integrate.quad(length, 0, np.pi / 2)
    perimeter = perimeter * 4 * a
    circle = 2 * np.pi * a
    Calculation1 = [perimeter, k, circle, circle / perimeter]
    c = c + 1
    perimeter = 0
    list1.append(Calculation1)
a = 20
c = 0
while c < a:
    k = c / a  # 이심률
    length = lambda theta: np.sqrt(1 - ((k ** 2) * (np.cos(theta) ** 2)))
    perimeter, _ = integrate.quad(length, 0, np.pi / 2)
    perimeter = perimeter * 4 * a
    circle = 2 * np.pi * a
    Calculation2 = [perimeter, k, circle, circle / perimeter]
    c = c + 1
    perimeter = 0
    list2.append(Calculation2)
a = 30
c = 0
while c < a:
    k = c / a  # 이심률
    length = lambda theta: np.sqrt(1 - ((k ** 2) * (np.cos(theta) ** 2)))
    perimeter, _ = integrate.quad(length, 0, np.pi / 2)
    perimeter = perimeter * 4 * a
    circle = 2 * np.pi * a
    Calculation3 = [perimeter, k, circle, circle / perimeter]
    c = c + 1
    perimeter = 0
    list3.append(Calculation3)

df1 = pd.DataFrame(list1)
df1.columns = ['타원의둘레', '이심률', '원의둘레', '비율']
df1.to_excel('장축10.xlsx')

df2 = pd.DataFrame(list2)
df2.columns = ['타원의둘레', '이심률', '원의둘레', '비율']
df2.to_excel('장축20.xlsx')

df3 = pd.DataFrame(list3)
df3.columns = ['타원의둘레', '이심률', '원의둘레', '비율']
df3.to_excel('장축30.xlsx')
