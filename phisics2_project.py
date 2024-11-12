import numpy as np #계산용 모델
import matplotlib.pyplot as plt #그래프 제작용 모델
import tensorflow as tf #인공 신경망 모델 제작용

# 물리적 상수
g = 9.8  # 중력 가속도 (m/s^2)
length = 10  # 줄 길이 (m)
mass = 10  # 진자 질량 (kg)
theta0 = np.pi / 4  # 초기 각도 (라디안)
omega0 = 0  # 초기 각속도 (rad/s)
dt = 0.01  # 시간 간격 (s)
t_max = 10  # 시뮬레이션 시간 (s)

# 초기화
time = np.arange(0, t_max, dt)
theta = np.zeros_like(time)
omega = np.zeros_like(time)
theta[0] = theta0
omega[0] = omega0

# 에너지를 저장할 리스트 초기화
kinetic_energy = []
potential_energy = []
total_energy = []
time_of_simulation = []

# 시뮬레이션
for t in time:
    alpha = - (g / length) * np.sin(theta[0])  # 각가속도
    omega[0] += alpha * dt  # 각속도 업데이트
    theta[0] += omega[0] * dt  # 각도 업데이트

    # 위치 에너지 (중력 퍼텐셜 에너지)
    pe = mass * g * length * (1 - np.cos(theta[0]))

    # 운동 에너지
    velocity = length * omega[0]
    ke = 0.5 * mass * velocity ** 2

    # 총 에너지
    te = ke + pe

    # 에너지 리스트에 추가
    potential_energy.append(pe)
    kinetic_energy.append(ke)
    total_energy.append(te)
    time_of_simulation.append(t)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(time, kinetic_energy, label='Kinetic Energy', color='blue')
plt.plot(time, potential_energy, label='Potential Energy', color='red')
plt.plot(time, total_energy, label='Total Energy', color='green', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Pendulum Energies Over Time')
plt.legend()
plt.grid(True)
plt.show()

#데이터 값 정리
xs = np.array(time_of_simulation)
ys = np.array(potential_energy)

#기본 그래프 생성
plt.plot(xs, ys, 'b.')
plt.show()

#인공 신경망 생성
#각 layer가 층을 뜻하고 input 레이어는 입력 층 마지막은 출력층임
model_f = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(1,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1,),
])

#최적화 함수 및 손실 함수 설정
model_f.compile(optimizer='rmsprop', loss='mse')

#모델 학습
model_f.fit(xs, ys, epochs=6000)

#모델 예측 값 저장
p_test = model_f.predict(xs)

#시각화
plt.plot(xs, ys, 'b.', label='actual')
plt.plot(xs, p_test, 'r.', label='predicted')
plt.legend()
plt.show()