import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

list1 = np.array([94, 95, 97, 103])
x_axis = np.array([1, 2, 3, 4])

model = LinearRegression()
'''
sorted_list = [[x] for x in list1]
sorted_x_list = [[x] for x in x_axis]

model.fit(sorted_x_list, sorted_list)

plt.scatter(x_axis, list1)
plt.plot(x_axis, model.coef_ * sorted_x_list + model.intercept_, color='red')
plt.show()
'''
second_sorted_x_list = np.column_stack((x_axis ** 2, x_axis))
second_sorted_list = np.column_stack((list1 ** 2, list1))

model.fit(second_sorted_x_list, list1)

print(model.coef_, model.intercept_)

plt.scatter(x_axis, list1)
plt.plot(x_axis, 1.25 * x_axis ** 2 - 3.35 * x_axis + 96.25, color='r')
plt.show()
print(1.25 * x_axis ** 2 - 3.35 * x_axis + 96.25)
