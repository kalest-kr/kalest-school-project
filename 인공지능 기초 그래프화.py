import pandas as pd
import matplotlib.pyplot as plt

x = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

# 엑셀 파일 읽기
file_path_seoul = 'C:/Users/ginok/PycharmProjects/pythonProject/서울특별시 진학률.xlsx'
df_seoul = pd.read_excel(file_path_seoul)

# 특정 열의 값 가져오기
column_name = '진학률'
column_values_of_seoul = df_seoul[column_name].tolist()

file_path_busan = 'C:/Users/ginok/PycharmProjects/pythonProject/부산광역시 진학률.xlsx'
df_busan = pd.read_excel(file_path_busan)

# 특정 열의 값 가져오기
column_name = '진학률'
column_values_of_busan = df_busan[column_name].tolist()

file_path_north_gyeongsan = 'C:/Users/ginok/PycharmProjects/pythonProject/경상북도 진학률.xlsx'
df_north_gyeongsan = pd.read_excel(file_path_north_gyeongsan)

# 특정 열의 값 가져오기
column_name = '진학률'
column_values_of_north_gyeongsan = df_north_gyeongsan[column_name].tolist()


file_path_south_gyeongsan = 'C:/Users/ginok/PycharmProjects/pythonProject/경상남도 진학률.xlsx'
df_south_gyeongsan = pd.read_excel(file_path_north_gyeongsan)

# 특정 열의 값 가져오기
column_name = '진학률'
column_values_of_south_gyeongsan = df_south_gyeongsan[column_name].tolist()


file_path_gyeonggy = 'C:/Users/ginok/PycharmProjects/pythonProject/경기도 진학률.xlsx'
df_gyeonggy = pd.read_excel(file_path_gyeonggy)

# 특정 열의 값 가져오기
column_name = '진학률'
column_values_of_gyeonggy = df_gyeonggy[column_name].tolist()


file_path_gangwon = 'C:/Users/ginok/PycharmProjects/pythonProject/강원도 진학률.xlsx'
df_gangwon = pd.read_excel(file_path_gangwon)

# 특정 열의 값 가져오기
column_name = '진학률'
column_values_of_gangwon = df_gangwon[column_name].tolist()

plt.plot(x, column_values_of_gangwon, 'b', label='gangwon', linewidth=1)
plt.plot(x, column_values_of_gyeonggy, 'r', label='gyeonggi', linewidth=1)
plt.plot(x, column_values_of_south_gyeongsan, 'g', label='south_gyeongsan', linewidth=1)
plt.plot(x, column_values_of_north_gyeongsan, 'y', label='north_gyeongsan', linewidth=1)
plt.plot(x, column_values_of_seoul, 'c', label='seoul', linewidth=1)
plt.legend()
plt.show()