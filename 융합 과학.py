from vpython import *
import numpy as np

# 기본 상수들
G = 6.67430e-11  # 중력 상수
M = 1.989e30  # 태양의 질량 (kg)
AU = 1.496e11  # 천문 단위 (m)

# 각 행성의 궤도 매개변수 정의 (긴반지름 a, 이심률 e, 공전 주기 T)
planets = [
    {"name": "Mercury", "a": 0.387 * AU, "e": 0.2056, "T": 0.241 * 365.25 * 24 * 3600, "color": color.gray(0.7)},
    {"name": "Venus", "a": 0.723 * AU, "e": 0.0067, "T": 0.615 * 365.25 * 24 * 3600, "color": color.orange},
    {"name": "Earth", "a": 1.000 * AU, "e": 0.0167, "T": 1.000 * 365.25 * 24 * 3600, "color": color.blue},
    {"name": "Mars", "a": 1.524 * AU, "e": 0.0935, "T": 1.881 * 365.25 * 24 * 3600, "color": color.red},
    {"name": "Jupiter", "a": 5.203 * AU, "e": 0.0489, "T": 11.862 * 365.25 * 24 * 3600, "color": color.orange},
    {"name": "Saturn", "a": 9.537 * AU, "e": 0.0565, "T": 29.457 * 365.25 * 24 * 3600, "color": color.yellow},
    {"name": "Uranus", "a": 19.191 * AU, "e": 0.0463, "T": 84.020 * 365.25 * 24 * 3600, "color": color.cyan},
    {"name": "Neptune", "a": 30.069 * AU, "e": 0.0100, "T": 164.8 * 365.25 * 24 * 3600, "color": color.blue}
]

# 특정 시간 t에서 행성의 위치를 계산하는 함수
def position(t, a, e, T):
    # 평균 이각
    M = (2 * np.pi / T) * t
    # 근사적으로 이각 E 찾기 (케플러 방정식 해결)
    E = M
    for _ in range(100):
        E = M + e * np.sin(E)
    # 진이각 계산
    theta = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
    r = a * (1 - e ** 2) / (1 + e * np.cos(theta))
    return r * np.cos(theta), r * np.sin(theta)

# 시뮬레이션 매개변수
dt = 365.25 * 24 * 3600 / 1000  # 시간 간격
num_steps = 1000000000000000000000000000000000000000000000000000000000000000000  # 시뮬레이션 스텝 수

# VPython 설정
scene = canvas(title='Kepler\'s Second Law Simulation',
               width=800, height=600, center=vector(0, 0, 0), background=color.black)

# 태양 객체 생성
sun = sphere(pos=vector(0, 0, 0), radius=AU / 20, color=color.yellow)

# 행성 객체 생성
planet_objects = []
for planet in planets:
    x, y = position(0, planet["a"], planet["e"], planet["T"])
    planet_sphere = sphere(pos=vector(x, y, 0), radius=AU / 50, color=planet["color"], make_trail=True)
    planet_objects.append({"sphere": planet_sphere, "params": planet})

# Earth 행성의 객체 찾기
earth = next(obj for obj in planet_objects if obj["params"]["name"] == "Earth")

# 지구 공전 수
earth_rotate_count = 0

# 초기 위치 검사 이전에 시뮬레이션 스텝 실행
for step in range(1, num_steps):  # 초기 조건을 제외하도록 1부터 시작
    t = step * dt
    rate(500)

    # 지구가 한 바퀴 돌았는지 확인
    if np.isclose(earth["sphere"].pos.y, 0, atol=1e-8) and earth["sphere"].pos.x > 0:
        earth_rotate_count += 1
        print(f"Earth has completed {earth_rotate_count} orbits.")

    # 각 행성의 위치 업데이트
    for planet_obj in planet_objects:
        planet = planet_obj["params"]
        x_pos, y_pos = position(t, planet["a"], planet["e"], planet["T"])
        planet_obj["sphere"].pos = vector(x_pos, y_pos, 0)

    # 모든 행성이 일렬로 나열되었는지 확인
    angles = [np.arctan2(planet_obj["sphere"].pos.y, planet_obj["sphere"].pos.x) for planet_obj in planet_objects]
    if all(np.isclose(angle, angles[0], atol=1e-2) for angle in angles):
        print('All planets are aligned.')
        break

print('Simulation stopped.')
print(f"Earth completed {earth_rotate_count} orbits.")

# 프로그램 실행을 유지
scene.waitfor('click')
