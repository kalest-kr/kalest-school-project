import pandas as pd

# 엑셀 파일을 읽어 데이터프레임으로 변환
df = pd.read_excel("C:/Users/ginok/OneDrive/바탕 화면/진학률 데이터.xlsx")

# 검색할 특정 값
target_value = '서울특별시'

# 특정 값을 가진 행을 찾기
row = df[df.isin([target_value]).any(axis=1)]

# 특정 값을 가진 행이 있는지 확인하고, 있다면 해당 행을 새로운 엑셀 파일로 저장
if not row.empty:
    # 새로운 엑셀 파일로 저장
    row.to_excel("서울특별시_데이터.xlsx", index=False)
    print("특정 값을 포함하는 행을 새로운 엑셀 파일로 저장했습니다.")
else:
    print("특정 값을 포함하는 행이 없습니다.")
#광주광역시 대구광역시 부산광역시 서울특별시
