from vpython import *
print("x,y,z 길이의 값을 차례대로 입력해주세요")
x_length = int(input())
y_length = int(input())
z_length = int(input())
# 평면 생성
platform1 = box(pos=vec(0, 5, 0), size=vec(x_length, y_length, z_length))
platform2 = box(pos=vec(0, 0, 0), size=vec(20, 0.1, 5), color=color.blue)


point1 = vector(x_length / 2, 5, z_length / 2)
point2 = vector(-x_length / 2, 5, z_length / 2)
point3 = vector(x_length / 2, 5, -z_length / 2)
point4 = vector(-x_length / 2, 5, -z_length / 2)


line1 = curve(pos=(point1, point2))
line2 = curve(pos=(point3, point4))


rotation_angle = int(input("회전할 각도를 지정해주세요.:", ))



# 기울기
angle = radians(rotation_angle)
axis = vector(0, 0, 1)  # 회전하는 기준이 되는 축
rotated_platform1 = platform1.rotate(angle=angle, axis=axis, origin=vec(0, 5, 0))
rotated_line1 = line1.rotate(angle=angle, axis=axis, origin=vec(0, 5, 2.5))
rotated_line2 = line2.rotate(angle=angle, axis=axis, origin=vec(0, 5, -2.5))


distance = 0.1
i = 0


while i <= 150:
    rate(100)
    rotated_platform1.pos.y -= distance
    point1.y -= distance
    point2.y -= distance
    point3.y -= distance
    point4.y -= distance

    i += 1

    if round(point1.y, 1) == platform2.pos.y:
        final_point1 = sphere(pos=point1, radius = 0.01)
    if round(point2.y, 1) == platform2.pos.y:
        final_point2 = sphere(pos=point2, radius = 0.01)
    if round(point3.y, 1) == platform2.pos.y:
        final_point3 = sphere(pos=point3, radius=0.01)
    if round(point4.y, 1) == platform2.pos.y:
        final_point4 = sphere(pos=point4, radius = 0.01)

overlap_x = min(final_point1.pos.x, final_point2.pos.x) * min(final_point3.pos.z, final_point4.pos.z)
print("Overlap area:", overlap_x)
