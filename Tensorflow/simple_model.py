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

def get_simple_regression_data():
  x = tf.random.uniform([100, 1], minval=0, maxval=20, dtype=tf.float32)
  y = x * 2  + 7 + tf.random.normal([100, 1])

  test_x = tf.random.uniform([10, 1], minval=0, maxval=20, dtype=tf.float32)
  test_y = test_x * 2  + 7 + tf.random.normal([10, 1])

  return (x, y), (test_x, test_y)  

def get_simple_classification_data():
  x = tf.random.uniform([100, 2], minval=0, maxval=20, dtype=tf.float32)
  y = tf.cast(x[:,1] + x[:,0] > 17, tf.float32)

  test_x = tf.random.uniform([10, 2], minval=0, maxval=20, dtype=tf.float32)
  test_y = tf.cast(test_x[:,1] + test_x[:,0] > 15, tf.float32)

  return (x, y), (test_x, test_y)