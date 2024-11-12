import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("C:/Users/ginok/OneDrive/바탕 화면/대기 이산화탄소 농도.xlsx", engine='openpyxl')

specific_column = df['B1']

list_of_data = [[x] for x in specific_column]

i = 1

list_of_x_axis = []

print(len(specific_column))

for i in range(len(specific_column)):
    list_of_x_axis.append(i)
    i += 1

sorted_x_axis = [[x] for x in list_of_x_axis]

model = LinearRegression()

model.fit(sorted_x_axis, list_of_data)

plt.plot(sorted_x_axis, list_of_data)
plt.plot(sorted_x_axis, model.coef_ * sorted_x_axis + model.intercept_, color='red')
plt.show()
