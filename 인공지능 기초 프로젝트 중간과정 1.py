import pandas as pd

df = pd.read_excel("C:/Users/ginok/PycharmProjects/pythonProject/서울특별시_데이터.xlsx")

# 합계를 구할 열 이름 (실제 엑셀 파일의 열 이름으로 대체)
column_name = '고등학교 졸업자 진학률(퍼센트)'  # 예시로 '졸업자수'라는 열 이름 사용

n = 0

list1 = []

while n < 3:

    # 합계를 구할 행 범위 (예: 10번째 행부터 20번째 행까지)
    start_row = 1 + 25 * n
    end_row = 25 + 25 * n

    # 범위 내의 값을 합산
    sum_value = df.loc[start_row:end_row, column_name].sum()

    print(sum_value / 31)

    value = [sum_value / 31]

    list1.append(value)

    n = n + 1

df = pd.DataFrame(list1)
df.columns = ['진학률']
df.to_excel('서울특별시 진학률.xlsx', index=False)