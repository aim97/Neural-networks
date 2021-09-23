from callbacks import TestingPlotCallback, LossPlotCallback
import tensorflow as tf
import tensorflow.keras as K
from tensorflow.keras.layers import Dense

def train_model(loss_fn, x, y, test_x, test_y, epochs_step = 10, steps = 5):
  model = K.Sequential([Dense(1, input_shape=(1,), activation='linear')])
  model.compile(optimizer='sgd', loss=loss_fn)

  model.fit(
    x, y, 
    epochs=epochs_step * steps, batch_size=32, verbose=0,
    callbacks=[
      TestingPlotCallback(epochs_step=epochs_step, steps=steps, test_data=(test_x, test_y)),
      LossPlotCallback(epochs_step=epochs_step, steps=steps)
    ]
  )