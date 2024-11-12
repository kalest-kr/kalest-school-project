from sklearn.model_selection import GridSearchCV
from tensorflow.keras.models import Sequential
from scikeras.wrappers import KerasClassifier
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Input
from sklearn.metrics import accuracy_score

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 784).astype('float32') / 255
x_test = x_test.reshape(-1, 784).astype('float32') / 255

# 모델을 생성하는 함수 정의
def create_model(first_layer_nodes=32, second_layer_nodes=16):
    model = Sequential()
    model.add(Input(shape=(784,)))  # Input 레이어를 명시적으로 추가
    model.add(Dense(first_layer_nodes, activation='relu'))
    model.add(Dense(second_layer_nodes, activation='relu'))
    model.add(Dense(10, activation='softmax'))  # 10개의 클래스 (MNIST)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# KerasClassifier로 래핑 (SciKeras 사용)
model = KerasClassifier(model=create_model, epochs=10, batch_size=128, verbose=0)

# 그리드 서치 설정
param_grid = {
    'model__first_layer_nodes': [16, 32, 64, 128, 256, 512, 1024, 2048],
    'model__second_layer_nodes': [8, 16, 32, 64, 128, 256, 512, 1024]
}

# GridSearchCV 실행
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3)
grid_result = grid.fit(x_train, y_train)

# 최적의 파라미터와 성능 출력
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

# 테스트 데이터로 최적의 모델 평가
best_model = grid_result.best_estimator_

# 테스트 데이터로 예측
y_pred = best_model.predict(x_test)

# 정확도 평가
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {test_accuracy:.4f}")

# 훈련 정확도와 테스트 정확도를 비교하여 과적합 확인
train_accuracy = grid_result.best_score_
print(f"Train Accuracy (Best Grid Search Result): {train_accuracy:.4f}")

