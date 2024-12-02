import matplotlib.pyplot as plt
import cv2
# tensorflow 2.12.0
# keras 3.2.0
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping



# CIFAR-10 데이터 세트를 불러옵니다.

(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# 데이터를 확인합니다.

print(train_images.shape, train_labels.shape)
print(test_images.shape, test_labels.shape)

# print(train_images[3])
# print(train_labels[3])

cv2.imshow('IMG', cv2.resize(train_images[3], (0,0), fx=10, fy=10) ) # 읽은 이미지를 화면에 표시      --- ③
# cv2.waitKey()  # 키가 입력될 때 까지 대기      --- ④
cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤

val_images = train_images[45000:]
val_labels = train_labels[45000:]

train_images = train_images[:45000]
train_labels = train_labels[:45000]

mlp_model = Sequential([
    Flatten(input_shape=(32, 32, 3)),
    Dense(512, activation='relu'),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
mlp_model.summary()

mlp_model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

history=mlp_model.fit(train_images, train_labels, epochs=5,
                      validation_data=(val_images, val_labels))
mlp_model.evaluate(test_images, test_labels)

# plt.plot(history.history['loss'], 'b--')
# plt.plot(history.history['val_loss'], 'r--')
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.legend(['train loss', 'validation loss'])
# plt.show()

predicted_labels = mlp_model.predict(test_images[:10])
print(predicted_labels)
predicted_results = tf.argmax(predicted_labels, axis=1)
print(predicted_results)
