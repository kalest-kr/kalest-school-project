from vpython import *
import numpy as np

# 그래픽 창 생성
scene = canvas(title='x^2 Graph', width=800, height=600)

# x축 생성
x_axis = cylinder(pos=vector(-10, 0, 0), axis=vector(20, 0, 0), radius=0.1, color=color.black)
# y축 생성
y_axis = cylinder(pos=vector(0, -10, 0), axis=vector(0, 20, 0), radius=0.1, color=color.black)

# x^2 그래프 그리기
x_vals = np.linspace(-5, 5, 100)
y_vals = x_vals**2

graph_x_squared = graph(title='x^2 그래프', xtitle='x', ytitle='x^2')
curve(pos=[vector(x, x**2, 0) for x in x_vals], color=color.blue)

# 그래프의 x축과 y축 설정
graph_x_squared.xmin = -5
graph_x_squared.xmax = 5
graph_x_squared.ymin = -10
graph_x_squared.ymax = 25

range_of_number = int(input("범위를 지정해 주세요: "))

i = -1/2

for number_2 in range(range_of_number):
    box(pos=vector(i, 0, 0), size=vector(1, number_2 ** 2, 0))
    i += 1




# 화면 업데이트
while True:
    rate(30)
