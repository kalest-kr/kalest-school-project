import pandas as pd

value = int(input('데이터의 개수를 지정해주세요'))

data = []

G = 6.67e-11

earth_mass = 5.9722 * (10 ** 24)

radius = 5177

rotation_speed = 1355

for value in range(value):
    weight = int(input('무게를 지정해주세요'))
    m = weight / 9.8 #질량 구하기
    F = G * ((m * earth_mass) / (6371 ** 2))#만유인력 계산
    F2 = m * 6371 * (rotation_speed ** 2)#외심력
    universial_gravitation = F / weight#만유인력의 차이
    Extrinsic_Force = F2 /weight#외심력의 차이
    DATA = [weight, F, F2, universial_gravitation, Extrinsic_Force]
    data.append(DATA)

df = pd.DataFrame(data)
df.columns = ['무게', '만유인력', '외심력', '만유인력%', '외심력%']
df.to_excel('중간작업2.xlsx', index=True)
