import keras
from PIL import Image
import os
import glob
import numpy as np

sorted_size = (160, 140)

class_names = ['강아지', '고양이']

dog_img = []
cat_img = []
dog_img_label = []
cat_img_label = []

# 이미지가 저장된 디렉터리 경로
directory_dog = "C:/Users/ginok/PycharmProjects/pythonProject/강아지"

# 지원하는 이미지 파일 확장자
image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif']

# 디렉터리 내 모든 이미지 파일 경로 가져오기
image_paths_dog = []
for ext in image_extensions:
    image_paths_dog.extend(glob.glob(os.path.join(directory_dog, ext)))

# 이미지를 하나씩 불러와서 리스트에 저장
for path in image_paths_dog:
    try:
        img = Image.open(path).convert('RGB')  # 이미지를 RGB로 변환
        width, height = img.size
        print(f"original size: {width} * {height}")
        resized_image = img.resize(sorted_size)
        dog_img.append(np.array(resized_image))
        dog_img_label.append(0)
        print(f'sorted size: {sorted_size[0]} x {sorted_size[1]}')
    except Exception as e:
        print(f"Error loading image {path}: {e}")

print(f"Loaded {len(dog_img)} dog images.")

# 고양이 이미지 불러오기
directory_cat = "C:/Users/ginok/PycharmProjects/pythonProject/고양이"
image_paths_cat = []
for ext in image_extensions:
    image_paths_cat.extend(glob.glob(os.path.join(directory_cat, ext)))

for path in image_paths_cat:
    try:
        img = Image.open(path).convert('RGB')  # 이미지를 RGB로 변환
        width, height = img.size
        print(f"original size: {width} * {height}")
        resized_image = img.resize(sorted_size)
        cat_img.append(np.array(resized_image))
        cat_img_label.append(1)
        print(f'sorted size: {sorted_size[0]} x {sorted_size[1]}')
    except Exception as e:
        print(f"Error loading image {path}: {e}")

print(f"Loaded {len(cat_img)} cat images.")

# 검증 데이터 불러오기
directory_val = "C:/Users/ginok/OneDrive/바탕 화면/검증 데이터"
image_paths_val = []
for ext in image_extensions:
    image_paths_val.extend(glob.glob(os.path.join(directory_val, ext)))

val_img_data = []
val_img_data_label = []

for path in image_paths_val:
    try:
        img = Image.open(path).convert('RGB')  # 이미지를 RGB로 변환
        width, height = img.size
        print(f"original size: {width} * {height}")
        resized_image = img.resize(sorted_size)
        val_img_data.append(np.array(resized_image))
        val_img_data_label.append(0)  # 검증 데이터의 레이블은 임의로 설정
        print(f'sorted size: {sorted_size[0]} x {sorted_size[1]}')
    except Exception as e:
        print(f"Error loading image {path}: {e}")

print(f"Loaded {len(val_img_data)} validation images.")

# 데이터를 numpy 배열로 변환
dog_img = np.array(dog_img)
dog_img_label = np.array(dog_img_label)
cat_img = np.array(cat_img)
cat_img_label = np.array(cat_img_label)
val_img_data = np.array(val_img_data)
val_img_data_label = np.array(val_img_data_label)

# 데이터의 형태 조정
combined_images = np.concatenate((dog_img, cat_img), axis=0)
combined_labels = np.concatenate((dog_img_label, cat_img_label), axis=0)

# 모델 정의
model = keras.Sequential()
model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same', input_shape=(160, 140, 3)))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(2, activation='softmax'))  # 클래스 수에 맞게 설정

model.summary()

# 모델 컴파일 및 학습
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.keras', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)

history = model.fit(
    combined_images, combined_labels, epochs=20,
    validation_data=(val_img_data, val_img_data_label),
    callbacks=[checkpoint_cb, early_stopping_cb]
)
