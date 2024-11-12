import sympy
from sympy import *
import numpy as np

print('**은 제곱을 뜻합니다')
print('*는 곱을 뜻합니다')

def final_changed_calculation(calculation):
    #기호로 정의
    x, y, z = sympy.sympify('x, y, z')

    #문자열을 공식화함
    try:
        changed_calculation = sympy.sympify(calculation)

        return changed_calculation
    except (sympy.SympifyError, ValueError) as e:
        return f"수식이 잘못되었거나 인식되지 않았습니다.: {e}"

while True:
    print('원하는 공식을 입력하세요')
    calculation = input('')
    result = final_changed_calculation(calculation) # 문자열을 공식으로 전환
    x = symbols('x')
    prime = Derivative(result, x).doit() #미분
    print('미분한 공식: ', prime)
    critical = sympy.solve(prime) # 극값의 좌표
    print('극값의 x좌표: ', critical)
    if calculation == 'break':
        break