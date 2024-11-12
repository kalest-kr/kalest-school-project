import matplotlib.pyplot as plt
import numpy as np

x = 0

print("x축의 개수를 지정해주세요")
repeat = int(input())

xaxis = []
yaxis = []
for repeat in range(repeat):
    x = x + 1
    xaxis.append(x)
    print("y축의 값을 입력해주세요")
    y = int(input())
    yaxis.append(y)

fig, ax = plt.subplots()
ax.bar(xaxis, yaxis, width = 1, edgecolor = "white", linewidth = 0.7)
ax.set(xlim = (0, max(xaxis)), xticks = np.arange(0, max(xaxis) + 1), ylim=(0, max(yaxis)), yticks=np.arange(min(yaxis), max(yaxis) + 1))
plt.show()