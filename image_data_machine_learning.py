from tensorflow import *
import keras
from PIL import Image
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

sorted_size = (160, 140)

class_names = ['강아지', '고양이']

dog_img = []
cat_img = []
dog_img_label = []
cat_img_label = []

# 이미지가 저장된 디렉터리 경로
directory = "C:/Users/ginok/PycharmProjects/pythonProject/강아지"

# 지원하는 이미지 파일 확장자
image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif']

# 디렉터리 내 모든 이미지 파일 경로 가져오기
image_paths = []
for ext in image_extensions:
    image_paths.extend(glob.glob(os.path.join(directory, ext)))

# 이미지를 하나씩 불러와서 리스트에 저장
for path in image_paths:
    try:
        img = Image.open(path)
        width, height = img.size
        print(f"original size: {width} * {height}")
        resized_image = img.resize(sorted_size)
        dog_img.append(np.array(resized_image))
        dog_img_label.append(0)
        width, height = resized_image.size
        print(f'sorted size: {width} x {height}')
    except Exception as e:
        print(f"Error loading image {path}: {e}")

# 불러온 이미지 개수 출력
print(f"Loaded {len(dog_img)} dog images.")

# 첫 번째 이미지를 예시로 보여주기
if dog_img:
    Image.fromarray(dog_img[0]).show()

directory_2 = "C:/Users/ginok/PycharmProjects/pythonProject/고양이"

# 디렉터리 내 모든 이미지 파일 경로 가져오기
image_paths_2 = []
for ext in image_extensions:
    image_paths_2.extend(glob.glob(os.path.join(directory_2, ext)))

for path in image_paths_2:
    try:
        img = Image.open(path)
        width, height = img.size
        print(f"original size: {width} * {height}")
        resized_image = img.resize(sorted_size)
        cat_img.append(np.array(resized_image))
        cat_img_label.append(1)
        width, height = resized_image.size
        print(f'sorted size: {width} x {height}')
    except Exception as e:
        print(f"Error loading image {path}: {e}")

print(f"Loaded {len(cat_img)} cat images.")

# 검증 데이터 디렉터리 경로
directory_3 = "C:/Users/ginok/OneDrive/바탕 화면/검증 데이터"

# 디렉터리 내 모든 이미지 파일 경로 가져오기
image_paths_3 = []
for ext in image_extensions:
    image_paths_3.extend(glob.glob(os.path.join(directory_3, ext)))

val_img_data = []
val_img_data_label = []

for path in image_paths_3:
    try:
        img = Image.open(path)
        width, height = img.size
        print(f"original size: {width} * {height}")
        resized_image = img.resize(sorted_size)
        val_img_data.append(np.array(resized_image))
        val_img_data_label.append(0)  # 여기서는 강아지로 레이블을 임의로 설정했습니다.
        width, height = resized_image.size
        print(f'sorted size: {width} x {height}')
    except Exception as e:
        print(f"Error loading image {path}: {e}")

print(f"Loaded {len(val_img_data)} validation images.")

if val_img_data:
    Image.fromarray(val_img_data[0]).show()

dog_img = np.array(dog_img)
dog_img_label = np.array(dog_img_label)
cat_img = np.array(cat_img)
cat_img_label = np.array(cat_img_label)
val_img_data = np.array(val_img_data)
val_img_data_label = np.array(val_img_data_label)

combined_images = np.concatenate((dog_img, cat_img), axis=0)
combined_labels = np.concatenate((dog_img_label, cat_img_label), axis=0)

print(f"Shape of combined images: {combined_images.shape}")
print(f"Shape of combined labels: {combined_labels.shape}")

model = keras.Sequential()

model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same', input_shape=(160, 140, 3)))

model.add(keras.layers.MaxPooling2D(2))

model.add(keras.layers.Conv2D(64, kernel_size=3, activation='relu', padding='same'))

model.add(keras.layers.MaxPooling2D(2))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(2, activation='softmax'))

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.keras', save_best_only=True)

early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)

history = model.fit(
    combined_images, combined_labels, epochs=20,
    validation_data=(val_img_data, val_img_data_label),
    callbacks=[checkpoint_cb, early_stopping_cb]
)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

model.evaluate(val_img_data, val_img_data_label)

preds = model.predict(val_img_data[0:1])
print(preds)

print(class_names[np.argmax(preds)])