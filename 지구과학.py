import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import keras
import tensorflow as tf
from sklearn.linear_model import LinearRegression

excel_file = openpyxl.load_workbook("C:/Users/ginok/Downloads/해양 온도.xlsx")

selected_sheet = excel_file.active
print(selected_sheet)

list_of_data = []
x_axis = []

a = 0
b = 0

data_col = selected_sheet['C']
for each in data_col:
    print(each.value)
    if a >= 1:
        list_of_data.append(each.value)
        x_axis.append(b)
    a += 1
    b += 1

print(list_of_data)
print(x_axis)
print(len(x_axis))

list_of_data = np.array(list_of_data)
x_axis = np.array(x_axis)

plt.plot(x_axis, list_of_data)
plt.show()
'''

#인공 신경망 생성
#각 layer가 층을 뜻하고 input 레이어는 입력 층 마지막은 출력층임
model_f = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1,),
])

#최적화 함수 및 손실 함수 설정
model_f.compile(optimizer='adam', loss='mse')

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.keras', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)

#모델 학습
model_f.fit(x_axis, list_of_data, epochs=1200, callbacks=[checkpoint_cb, early_stopping_cb])

#모델 예측 값 저장
p_test = model_f.predict(x_axis)

#시각화
plt.plot(x_axis, list_of_data, 'b.', label='actual')
plt.plot(x_axis, p_test, 'r.', label='predicted')
plt.legend()
plt.show()
'''
model = LinearRegression()

list_of_data = [[x] for x in list_of_data]
x_axis = [[x] for x in x_axis]

print(list_of_data)
print(x_axis)

model.fit(x_axis, list_of_data)

plt.plot(x_axis, list_of_data)
plt.plot(x_axis, model.coef_ * x_axis + model.intercept_, color='r')
plt.show()
