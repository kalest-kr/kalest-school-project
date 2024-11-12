import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import csv

df = pd.read_excel("C:/Users/ginok/Downloads/경기도시군별온실가스배출량.xlsx")

df2 = pd.read_excel("C:/Users/ginok/Downloads/경상남도 김해시_통계지수_평균기온_20211231.xlsx")

# 합계를 구할 열 이름 (실제 엑셀 파일의 열 이름으로 대체)
column_name = '온실가스배출량(tonCO2-eq)'

column_name2 = '평균기온(섭씨)'

n = 0

list1 = []

while n < 4:

    # 합계를 구할 행 범위 (예: 10번째 행부터 20번째 행까지)
    start_row = 0 + 31 * n
    end_row = 30 + 31 * n

    # 범위 내의 값을 합산
    sum_value = df.loc[start_row:end_row, column_name].sum()

    print(sum_value / 31)

    value = [sum_value / 31]

    list1.append(value)

    n = n + 1


tempretur_value_list = []

print(list1)

x_axis = ['2018', '2019', '2020', '2021']

plt.plot(x_axis, list1)
plt.show()

x_axis_2 = [[1], [2], [3], [4]]

#선형회귀 분석
model = LinearRegression()

model.fit(x_axis_2, list1)

plt.plot(x_axis_2, list1)
plt.plot(x_axis_2, model.coef_ * x_axis_2 + model.intercept_)
plt.show()

a = 0

while a < 5:
    start_row = 0 + 85 * a
    end_row = 84 + 85 * a

    sum_value = df2.loc[start_row:end_row, column_name2].sum()

    value = sum_value / 85

    tempretur_value_list.append(value)

    a += 1

#기온
x_axis = ['2017', '2018', '2019', '2020', '2021']
plt.plot(x_axis, tempretur_value_list)
plt.show()

x_axis_2 = [[1], [2], [3], [4], [5]]

model.fit(x_axis_2, tempretur_value_list)

plt.plot(x_axis_2, tempretur_value_list)
plt.plot(x_axis_2, model.coef_ * x_axis_2 + model.intercept_)
plt.show()
