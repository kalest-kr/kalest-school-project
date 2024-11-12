from sympy import symbols, sympify, integrate

# 사용자로부터 수식 입력 받기
expression_str = input("적분할 식을 입력하세요: ")

# 사용자로부터 적분 범위 입력 받기
var = symbols('x')
lower_limit = float(input("하한 값을 입력하세요: "))
upper_limit = float(input("상한 값을 입력하세요: "))

# 입력된 수식을 SymPy 심볼로 변환
expression = sympify(expression_str.replace('^', '**').replace('x', '*x'))

# 적분 수행
integral = integrate(expression, (var, lower_limit, upper_limit))

print(f"적분 결과: {integral}")
