from PIL import Image, ImageDraw, ImageFont

# 빈 이미지 생성 (RGB, 크기: 500x500, 색상: 흰색)
image = Image.new("RGB", (800, 800), color="white")

# 이미지를 조작할 도구 생성
draw = ImageDraw.Draw(image)

x_start = 0
x_end = 100
y_start = 0
y_end = 100

# 직사각형 그리기
for x in range(0, 4):
    for i in range(0, 4):
        draw.rectangle((x_start, y_start, x_end, y_end), fill="white", outline="black")
        y_start += 100
        y_end += 100
        draw.rectangle((x_start, y_start, x_end, y_end), fill="green", outline="black")
        y_start += 100
        y_end += 100
    x_start += 100
    x_end += 100
    y_start = 0
    y_end = 100
    for i in range(0, 4):
        draw.rectangle((x_start, y_start, x_end, y_end), fill="green", outline="black")
        y_start += 100
        y_end += 100
        draw.rectangle((x_start, y_start, x_end, y_end), fill="white", outline="black")
        y_start += 100
        y_end += 100
    x_start += 100
    x_end += 100
    y_start = 0
    y_end = 100

# 이미지 저장
image.save("generated_image.png")

# 이미지 보기
image.show()

board = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f8', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f8', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f8', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f8', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f8', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f8', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f8', 'g1', 'h1']
]