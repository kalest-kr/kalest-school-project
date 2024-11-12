'''
import tensorflow as tf
import numpy as np

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0])
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0])

model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(shape=(1, )),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(xs, ys, epochs=500)

p = model.predict(np.array([10.0]))

print('p:', p)
'''

'''

#2차 함수의 근사 프로그램
import numpy as np
import time
import matplotlib.pyplot as plt
import tensorflow as tf

NUM_SAMPLES = 1000

np.random.seed(int(time.time()))

xs = np.random.uniform(-2, 0.5, NUM_SAMPLES)
np.random.shuffle(xs)
print(xs[:5])

ys = 2 * xs ** 2 + 3 * xs + 5
print(ys[:5])

plt.plot(xs, ys, 'b.')
plt.show()

ys += 0.1 * np.random.randn(NUM_SAMPLES)

plt.plot(xs, ys, 'g.')
plt.show()

NUM_SPLIT = int(0.8 * NUM_SAMPLES)

x_train, x_test = np.split(xs, [NUM_SPLIT])
y_train, y_test = np.split(ys, [NUM_SPLIT])

plt.plot(x_train, y_train, 'b.', label='train')
plt.plot(x_test, y_test, 'r.', label='test')
plt.legend()
plt.show
#실제 학습 전 그래프

model_f = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(1, )),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)
])

model_f.compile(optimizer='rmsprop', loss='mse')

p_test = model_f.predict(x_test)

plt.plot(x_test, y_test, 'b.', label='actual')
plt.plot(x_test, p_test, 'r.', label='predicted')
plt.legend()
plt.show()

model_f.fit(x_train, y_train, epochs=600)

p_test = model_f.predict(x_test)

plt.plot(x_test, y_test, 'b.', label='actual')
plt.plot(x_test, p_test, 'r.', label='predicted')
plt.legend()
plt.show()
#학습 후 그래프
'''

# 5차 함수 근사
import numpy as np
import time
import time
import matplotlib.pyplot as plt
import tensorflow as tf

start_time = time.time()

NUM_SAMPLES = 1000

np.random.seed(int(time.time()))

xs = np.random.uniform(-2, 2, NUM_SAMPLES)
np.random.shuffle(xs)
print(xs[:5])

ys = (xs + 1.7) * (xs + 0.7) * (xs - 0.3) * (xs - 1.3) * (xs - 1.9) + 0.2
print(ys[:5])
'''
plt.plot(xs, ys, 'b.')
plt.show()
'''
ys += 0.1 * np.random.randn(NUM_SAMPLES)
'''
plt.plot(xs, ys, 'g.')
plt.show()
'''
NUM_SPLIT = int(0.8 * NUM_SAMPLES)

x_train, x_test = np.split(xs, [NUM_SPLIT])
y_train, y_test = np.split(ys, [NUM_SPLIT])
'''
plt.plot(x_train, y_train, 'b.', label='train')
plt.plot(x_test, y_test, 'r.', label='test')
plt.legend()
plt.show
#실제 학습 전 그래프
'''
model_f = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(1, )),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)
])

# rmsprop, sgd, adam, adagrad, adadelta
model_f.compile(optimizer='rmssprop', loss='mse')

p_test = model_f.predict(x_test)

'''
plt.plot(x_test, y_test, 'b.', label='actual')
plt.plot(x_test, p_test, 'r.', label='predicted')
plt.legend()
plt.show()
'''

model_f.fit(x_train, y_train, epochs=600)

p_test = model_f.predict(x_test)

plt.plot(x_test, y_test, 'b.', label='actual')
plt.plot(x_test, p_test, 'r.', label='predicted')
plt.legend()
plt.show()
#학습 후 그래프

end_time = time.time()

print(end_time - start_time)
