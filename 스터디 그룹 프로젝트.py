import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import nltk

replace_dict = {
    'X': '0',
    '주의보': '1',
    '경보': '1'
}


def reading_exel(x):
    df = pd.read_csv(x, encoding='cp949')
    column1_data = df.iloc[:, 9].replace(replace_dict)
    column1_data = column1_data.astype('int')
    total = sum(column1_data)
    print(total)

reading_exel("C:\한파 데이터셋 csv.ver\sheet1.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet2.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet3.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet4.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet5.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet6.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet7.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet8.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet9.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet10.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet11.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet12.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet13.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet14.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet15.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet16.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet17.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet18.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet19.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet20.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet21.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet22.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet23.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet24.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet25.csv")
reading_exel("C:\한파 데이터셋 csv.ver\sheet26.csv")