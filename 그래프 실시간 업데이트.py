import sympy
from sympy import *
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

x_list = []
y_list = []

def final_changed_calculation(calculation):
    #기호로 정의
    x, y, z = sympy.sympify('x, y, z')

    #문자열을 공식화함
    try:
        changed_calculation = sympy.sympify(calculation)

        return changed_calculation
    except (sympy.SympifyError, ValueError) as e:
        return f"수식이 잘못되었거나 인식되지 않았습니다.: {e}"

x = -100

while True:
    print('원하는 공식을 입력하세요')
    calculation = input('')
    result = final_changed_calculation(calculation) # 문자열을 공식으로 전환
    x = symbols('x')
    plot(result)

