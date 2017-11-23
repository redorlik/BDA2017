import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.datasets import mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0],28*28)
x_test = x_test.reshape(x_test.shape[0],28*28)

x_train = x_train.astype('float32')
x_train = x_train/255.

x_test = x_test.astype('float32')
x_test = x_test/255.

num_classes = 10
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()

model.add(Dense(512, activation='relu', input_shape=(28*28,)))
#model.add(Dropout(0.1))
hid = Dense(512, activation='relu')
model.add(hid)
#model.add(Dropout(0.1))
out = Dense(10, activation='softmax')
model.add(out)
print(model.summary())

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])
print(x_train.shape)
model.fit(x_train, y_train,
          epochs=20,
          batch_size=128,
          verbose=1,
                    validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, batch_size=128)
