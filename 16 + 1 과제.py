from vpython import *
import ast
'''
#예제 1
#물리 성질 초기화
f = 2 # 힘

m = 1#질량

a = f/m #가속도

print("가속도 =", a, "m/s^2")

'''
'''
#뉴턴의 제 3 법칙( 지구와 달 사이의 인력과 가속도 계산)

scale_factor = 5.0 # 크기 조정을 위한 변수

#상수 초기화
r = 384400000# 지구와 달 사이의 거리
g = 6.67e-11#만유인력상수

# 지구와 달 만들기
earth = sphere(pos = vec(0, 0, 0), radius=scale_factor * 6371000, texture = textures.earth)
moon = sphere(pos=vec(r,0,0), radius = scale_factor * 1731000, color = color.white)

#물리 성질 초기화
earth.mass = 5.97e24
moon.mass = 7.347e22

#지구와 달 사이의 인력
F = g * earth.mass * moon.mass / r ** 2

#뉴턴의 제 3법칙 적용(작용 반작용)
earth.force = F
moon.force = -F

#지구와 달 사이의 인력 출력
print("earth.force = ", earth.force, "N")
print("moon.force = ", earth.force, "N")

#가속도 계산
earth.acc = F/earth.mass
moon.acc = F/moon.mass

#지구와 달의 가속도 출력
print("earth.acc = ", earth.acc, "m/s^2")
print("moon.acc =", moon.acc, "m/s^2")'''
'''
x_axis = arrow(axis=vec(10, 0, 0), color=color.red, shaftwidth=0.1)
y_axis = arrow(axis=vec(0, 10, 0), color=color.blue, shaftwidth=0.1)
z_axis = arrow(axis=vec(0, 0, 10), color=color.green, shaftwidth=0.1)

ball = sphere(pos=vec(6, 10, 4), radius=0.2)

#스칼라 곱 계산
#ball.pos = ball.pos * 2.0
#ball.pos = ball.pos / 2
print("ball.pos =", ball.pos)
#sqrt = 루트하는 명령어
#벡터의 크기 계산
ball.mag = mag(ball.pos)
check_ball_mag = sqrt(ball.pos.x ** 2 + ball.pos.y ** 2 + ball.pos.z ** 2)
print("ball.mag =", ball.mag)
print("check! mag.:", check_ball_mag)

#단위 벡터 계산
ball.dir = ball.pos /ball.mag

#ball.dir = norm(ball.pos)

print("ball.dir=", ball.dir)
print("check! mag of unit vector:", mag(ball.dir))

#원점에서 ball을 가리키는 벡터 표현
pos_vec = arrow(pos=vec(0, 0, 0), axis=ball.pos, color=color.yellow, shaftwidth=0.2)
pos_vec2 = arrow(pos=vec(0, 0, 0), axis=ball.pos / 10, color=color.white, shaftwidth=0.3)

print(ball.pos)
'''
'''
a = vec(1, 2, 3)
b = vec(1.01, 2, 3)

if a.x == b.x and a.y == b.y and a.z == b.z:
    print("equal")
else:
    print("not equal")

#시뮬레이션에서는 두 값의 차이가 tol보다 작다면 같은 값으로 간주하는 경우도 있음
#abs는 절대값
tol = 0.1
if abs(a.x - b.x) < tol and abs(a.y - b.y) < tol and abs(a.z - b.z) < tol:
    print("equal")
else:
    print("not equal")
'''
'''
a = vec(1, 2, 3)
b = vec(-4, 5, 6)

#합차 벡터 지정
c = a + b
d = a - b

print(c, d)

#벡터의 합
a_vec = arrow(pos=(vec(0, 0, 0)), axis=a, shaftwidth=0.1)
b_vec = arrow(pos=a, axis=b, shaftwidth=0.1)
c_vec = arrow(pos=vec(0, 0, 0), axis=c, shaftwidth=0.1, color=color.red)

#벡터의 차
a_vec_2 = arrow(pos=vec(0, 0, 0), axis=a, shaftwidth=0.1, color=color.yelow)
b_vec_2 = arrow(pos=vec(0, 0, 0), axis=b, shaftwidth=0.1, color=color.yellow)
d_vec_2 = arrow(pos=b, axis=d, shaftwidth=0.1, color=color.blue)
'''
'''
scale_factor = 5.0

#지구
earth = sphere(pos=vec(0, 0, 0), radius=scale_factor * 6371000, texture=textures.earth)

#사과
apple = sphere(pos=vec(0, (scale_factor * 6371000) + 1000000, 0), radius=100000, color=color.red)

#질량
earth.mass = 5.9722 * (10 ** 24)
apple.mass = 1000

#만유인력
g = 6.67e-11

#거리(대충함)
r = 1000000

#인력
F = g * earth.mass * apple.mass / r ** 2


apple.force = vec(0, -F, 0)


#가속도 계산
apple.acc = F/apple.mass

#화살표 생성
apple_gravity = arrow(pos=apple.pos, axis=vec(0, -F, 0), shaftwidth=20000, color=color.green)
apple_acc = arrow(pos=apple.pos, axis=vec(0, apple.acc, 0), shaftwidth=30000, color=color.blue)

#새 변수 생성
apple_acc2 = vec(0, -F/apple.mass, 0)

#전부 더한 변수
a = apple.force + apple_acc2

#생성
a_arrow = arrow(pos=apple.pos, axis=a, shaftwidth=10000, color=color.white)

print('apple acc:', apple.acc)
print('apple gravity:', F)
'''
'''
pos_i = vec(-5, 0, 0)
v_i = vec(0.1, 0, 0)
acc = vec(0.1, 0, 0)

cart = box(pos = pos_i, size = vec(0.3, 0.3, 0.3), color=color.yellow, make_trail=True, trail_type="points", trail_radius=0.02, interval=2)
acart = box(pos=pos_i + vec(0, 1, 0), size=vec(0.3, 0.3, 0.3), color=color.white, make_trail=True, trail_type="points", trail_radius=0.02, interval=2)

cart.v = v_i
acart.v = v_i
scale = 2
attach_arrow(cart, "v", scale=2, shaftwidth=0.1)
#cart_veil=arrow(pos=cart.pos, axis=scale*cart.v, shaftwidth=0.1)

scene.autoscale = False

t = 0
dt = 0.1

while t < 10:
    rate(30)
    cart.v = cart.v + acc * dt
    cart.pos = cart.pos + cart.v * dt
    t = t + dt

    acart.pos = pos_i + vec(0, 1, 0) + v_i * t + 0.5 * acc * t ** 2
    print(cart.pos, acart.pos, abs(acart.pos.x - cart.pos.x))
'''
'''
# 공 바닥
ball = sphere(radius=0.2)
ground = box(pos=vec(0, -4, 0), size=vec(15, -0.01, 5))
# 초기설정
ball.pos = vec(-2, 0, 0)
ball.v = vec(1, 1, 0)
ball.a = vec(0, -0.35, 0)

t = 0
dt = 0.01
# 화살표 부착
attach_arrow(ball, "v", shaftwidth=0.1, color=color.green)
attach_arrow(ball, "a", shaftwidth=0.05, color=color.red)
# 자취 그리기
attach_trail(ball, type="points", pps=5)
# 그래프
motion_graph = graph(title='position-time', xtitle='t', ytitle='y')
g_bally = gcurve()
motion_graph2 = graph(title='velocity-time', xtitle='t', ytitle='vy')
g_ballvy = gcurve(color=color.green)

# 시뮬레이션 루프
while ball.pos.y > ground.pos.y:
    rate(1 / dt)
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt
    g_bally.plot(pos=(t, ball.pos.y))
    g_ballvy.plot(pos=(t, ball.v.y))
    t = dt + t
'''


#생성
sun = sphere(pos=vec(0, 0, 0), radius=1390000, color=color.yellow,)
earth = sphere(pos=vec(0, 149600000 + 1390000, 0), radius=6400, texture=textures.earth, make_trail=True,
               trail_type='curve', trail_radius=3000000)
moon = sphere(pos=vec(0, 152764405, 0), radius=1700, color=color.white, make_trail=True, trail_type='curve',
             trail_radius=3000000, retain=1000)

#지점 잡기
start_point = vec(0, -(149600000 + 1390000), 0)
end_point = vec(0, 149600000 + 1390000, 0)

#선 생성
line1 = curve(pos=[start_point, end_point], visible=True)

#기초 값 생성
i = 0
rotation_axis = vec(0, 0, 1)




while True:
    rate(30)
    i -= 1
    a = radians(i)

    line1.rotate(angle=(pi / i), axis=rotation_axis)
    point = line1.slice(1, 2)

    clean_point = {k: v for d in point for k, v in d.items()}
    clean_point_value = list(clean_point.values())

    end_point = sphere(pos=vec(*clean_point_value), visible=True, radius=300000)


    earth.pos = end_point.pos

    print(earth.pos)
    print('end_point:', end_point.pos)
    print('point:', point)
