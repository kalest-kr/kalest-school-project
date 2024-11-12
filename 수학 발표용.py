from sympy import symbols, integrate, simplify


def calculate_integral(expression):
    x = symbols('x')
    try:
        # 입력된 수식에서 2x를 2*x로 변환하여 SymPy에서 인식 가능하도록 함
        expression = expression.replace('2x', '2*x')

        integrated_expr = integrate(expression, x)
        integrated_expr = simplify(integrated_expr)
        return integrated_expr
    except Exception as e:
        return f"적분을 계산하는 동안 오류가 발생했습니다: {e}"


def main():
    user_input = input("적분할 식을 입력하세요: ")
    result = calculate_integral(user_input)
    print(f"적분 결과: {result}")


if __name__ == "__main__":
    main()
