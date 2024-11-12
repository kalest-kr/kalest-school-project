import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/NGULIM.TTF"

font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

years = [2014, 2018, 2023]
value = [397, 407, 419]
plt.plot(years, value, color='green', marker='o', linestyle='solid')
plt.title('이산화탄소 농도')
plt.ylabel('이산화탄소 농도(ppm)')
plt.xlabel('년도')
plt.grid(True)
plt.show()

data = [[14.3],
        [9.8],
        [13.4],
        [11.5],
        [8.9],
        [8.3],
        [6.3]
        ]

x = np.arange(1)

plt.bar(x+0.00, data[0], color='r', width=0.25, edgecolor='k')
plt.bar(x+0.25, data[1], color='orange', width=0.25, edgecolor='k')
plt.bar(x+0.50, data[2], color='yellow', width=0.25, edgecolor='k')
plt.bar(x+0.75, data[3], color='green', width=0.25, edgecolor='k')
plt.bar(x+1.00, data[4], color='cyan', width=0.25, edgecolor='k')
plt.bar(x+1.25, data[5], color='b', width=0.25, edgecolor='k')
plt.bar(x+1.50, data[6], color='purple', width=0.25, edgecolor='k')
plt.xticks((0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50), ('인천', '서울', '울산', '부산', '대전', '대구', '광주'))
plt.title('지역별 열대야 증가')
plt.ylabel('일(day)')
plt.xlabel('지역')
plt.show()

years = ['1950', '2010']
value = [21.3, 23.6]
plt.plot(years, value, color='b', marker='o', linestyle='solid')
plt.ylabel('평균온도')
plt.xlabel('년도')
plt.title('대구 6월 평균 기온')
plt.show()

N = 2

cocoa_value = (1.89, 2.25)
orange_value = (3.12, 4.31)

ind = np.arange(N)
width = 0.35

p1 = plt.bar(ind, cocoa_value, width, color='r')
p2 = plt.bar(ind, orange_value, width, bottom=cocoa_value)

plt.ylabel('비용(달러)')
plt.xticks(ind, ('1월', '7월'))
plt.legend((p1[0], p2[0]), ('코코아', '오렌지 쥬스'))
plt.show()

years = ['2014', '2023']
data = [1910, 2640]
plt.plot(years, data, color='cyan', marker='o', linestyle='solid')
plt.ylabel('인구 수(만명)')
plt.xlabel('년도')
plt.show()