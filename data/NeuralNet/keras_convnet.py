import keras
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten
from keras.datasets import mnist
import keras.backend as be

num_classes = 10

(x_train,y_train),(x_test,y_test) = mnist.load_data()

if be.image_data_format() == "channels_first":
    x_train = x_train.reshape(x_train.shape[0],1,28,28)
    x_test = x_test.reshape(x_test.shape[0],1,28,28)
    shape = (1,28,28)
else:
    x_train = x_train.reshape(x_train.shape[0],28,28,1)
    x_test = x_test.reshape(x_test.shape[0],28,28,1)
    shape = (28,28,1)

y_train = keras.utils.to_categorical(y_train,num_classes)
y_test = keras.utils.to_categorical(y_test,num_classes)

model = Sequential()
inp = Conv2D(32,activation="relu",kernel_size=(3,3),
            input_shape=shape)
model.add(inp)
pool = MaxPooling2D(pool_size=(2, 2))
model.add(pool)
hid1 = Conv2D(64,activation="relu",kernel_size=(3,3))
model.add(hid1)
pool = MaxPooling2D(pool_size=(2, 2))
model.add(pool)
model.add(Flatten())
out = Dense(num_classes,activation="softmax")
model.add(out)

model.compile(optimizer="SGD",loss="categorical_crossentropy",
                metrics=["accuracy"])
model.fit(x_train,y_train,epochs=20,batch_size=128)
