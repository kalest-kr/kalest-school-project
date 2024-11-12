from vpython import *

print("x, y, z 길이의 값을 차례대로 입력해주세요")
x_length = int(input())
y_length = int(input())
z_length = int(input())

# 평면 생성
platform1 = box(pos=vec(0, 5, 0), size=vec(x_length, y_length, z_length), color=color.red)
platform2 = box(pos=vec(0, 0, 0), size=vec(20, 1, 5), color=color.blue)

point1 = vector((x_length / 2), 5, (z_length / 2))
point2 = vector((-x_length / 2), 5, (z_length / 2))
point3 = vector((x_length / 2), 5, (-z_length / 2))
point4 = vector((-x_length / 2), 5, (-z_length / 2))

line1 = curve(pos=(point1, point2), color=color.green)
line2 = curve(pos=(point3, point4), color=color.green)

rotation_angle = int(input("회전할 각도를 지정해주세요: "))

# 기울기
angle = radians(rotation_angle)
axis = vector(0, 0, 1)  # 회전하는 기준이 되는 축
platform1.rotate(angle=angle, axis=axis, origin=vec(0, 5, 0))
line1.rotate(angle=angle, axis=axis, origin=vec(0, 5, (z_length / 2)))
line2.rotate(angle=angle, axis=axis, origin=vec(0, 5, (-z_length / 2)))

distance = 0.1
i = 0

overlap_x = 0  # 겹치는 영역 초기화

while i <= 150:
    rate(100)
    platform1.pos.y -= distance
    point1.y -= distance
    point2.y -= distance
    point3.y -= distance
    point4.y -= distance

    i += 1

    if round(point1.y, 1) == platform2.pos.y:
        final_point1 = point1
    if round(point2.y, 1) == platform2.pos.y:
        final_point2 = point2
    if round(point3.y, 1) == platform2.pos.y:
        final_point3 = point3
    if round(point4.y, 1) == platform2.pos.y:
        final_point4 = point4

    if 'final_point1' in locals() and 'final_point2' in locals() and 'final_point3' in locals() and 'final_point4' in locals():
        overlap_x = max(0, min(final_point1.x, final_point2.x) - max(final_point3.x, final_point4.x))
        overlap_y = max(0, min(final_point1.y, final_point2.y) - max(final_point3.y, final_point4.y))
        overlap_z = max(0, min(final_point1.z, final_point2.z) - max(final_point3.z, final_point4.z))
        overlap_volume = overlap_x * overlap_y * overlap_z
        print("Overlap volume:", overlap_volume)
        break
