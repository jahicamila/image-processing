import numpy as np
import keras
from keras import layers
from keras.datasets import mnist
from keras.models import Sequential

# Učitavanje MNIST dataseta
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizacija vrijednosti piksela na raspon od 0 do 1
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Pretvaranje slika iz 2D oblika u 3D oblik (dodavanje kanala)
x_train = np.expand_dims(x_train, axis=-1)
x_test = np.expand_dims(x_test, axis=-1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Kreiranje modela
model = keras.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.2))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.2))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(layers.Dropout(0.2))

model.add(Dense(10, activation='softmax'))
model.add(layers.Dropout(0.2))

model.summary()

# Kompajliranje modela
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treniranje modela
model.fit(x_train, y_train, epochs=10, batch_size=128, validation_split=0.1)

# Evaluacija modela
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)


img=x_test[2345]
img=img.reshape(1,28,28,1)
score = model.predict(img)
score_classes = np.argmax(score, axis=1)
img=x_test[2345]
plt.imshow(img)
plt.waitforbuttonpress(0)
print('Cifra   je:',score_classes)
