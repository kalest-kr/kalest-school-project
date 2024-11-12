import numpy as np
import matplotlib.pyplot as plt

a = 10
c = 9
x_pos = 1
y_pos = 0

list_of_y_value = []
list_of_x_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]


while a > x_pos:

    b_double = a ** 2 - c ** 2

    b = np.sqrt(b_double)

    number_regulation = ((10 ** 2) * (b ** 2) - (b ** 2) * (x_pos ** 2)) / 100

    y_pos = np.sqrt(number_regulation)

    Slope_of_tangent = -((b ** 2) / (a ** 2)) * (x_pos / y_pos)

    list_of_y_value.append(Slope_of_tangent)

    x_pos += 1

print(list_of_y_value)

plt.plot(list_of_x_value, list_of_y_value)
plt.show()