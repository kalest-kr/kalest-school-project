import numpy as np
from scipy import integrate

a = 10

c = 1

def ellipse_perimeter(a, b):
    e_squared = c / a  # 타원의 이심률 제곱 계산
    integrand = lambda theta: np.sqrt(1 - e_squared * np.sin(theta) ** 2)  # 적분할 함수 정의

    # 0부터 pi/2까지의 적분 계산
    perimeter, _ = integrate.quad(integrand, 0, np.pi / 2)

    # 타원의 둘레 계산
    perimeter *= 4 * a

    return perimeter


# 장축과 단축의 길이 설정
a = 10  # 장축의 반지름
b = 5  # 단축의 반지름

# 타원의 둘레 계산
perimeter = ellipse_perimeter(a, b)
print("타원의 둘레:", perimeter)
