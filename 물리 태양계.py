from vpython import *

#생성
sun = sphere(pos=vec(0, 0, 0), radius=13900, color=color.yellow,)
earth = sphere(pos=vec(0, 149600, 0), radius=6400, texture=textures.earth, make_trail=True, trail_type='curve', trail_radius=300, retain=1000)
moon = sphere(pos=vec(0, 152764, 0), radius=1700, color=color.white, make_trail=True, trail_type='curve', trail_radius=300, retain=1000)


#지구와 달 사이의 거리
r1 = 384405

#태양과 지구 사이의 거리
r2 = 149600

while True:
    rate(30)

    if earth.pos.x >= 0 and earth.pos.y > 0:
        earth.pos.x += 100
        earth.pos.y = sqrt(r2 ** 2 - earth.pos.x ** 2)
        if (r2 ** 2 - earth.pos.x ** 2) < 0:
            earth.pos = vec(r2, 0, 0)
            earth.pos.x -= 100
            earth.posy = sqrt(r2 ** 2 - earth.pos.x ** 2)
    if earth.pos.x > 0 and earth.pos.y <= 0:
        earth.pos.x -= 100
        earth.pos.y = -(sqrt(abs(r2 ** 2 - earth.pos.x ** 2)))
    if earth.pos.x <= 0 and earth.pos.y < 0:
        earth.pos.x -= 100
        earth.pos.y = -(sqrt(r2 ** 2 - earth.pos.x ** 2))
    if earth.pos.x < 0 and earth.pos.y >= 0:
        earth.pos.x += 100
        earth.pos.y = sqrt(abs(r2 ** 2 - earth.pos.x ** 2))
    if earth.pos.x==-r2 and earth.pos.y == 0:
        print('?')
