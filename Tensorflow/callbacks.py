import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

class TestingPlotCallback(tf.keras.callbacks.Callback):
  def __init__(self, steps = 5, epochs_step=10, test_data=None):
    super(TestingPlotCallback, self).__init__()
    self.epochs_step = epochs_step
    
    rows = (steps + 4) // 5
    cols = 5

    self.fig = plt.figure(figsize=(20, rows * 2))
    self.fig.suptitle('Test Prediction vs Test samples', fontsize=10, color='forestgreen')
    
    self.plots = self.fig.subplots(rows, cols).flatten()
    self.test_data = test_data

  def on_epoch_end(self, epoch, logs={}):
    mark = self.epochs_step - 1
    if epoch > 0 and epoch % mark == 0:
      step = epoch // mark - 1
      test_x, test_y = self.test_data
      ax = self.plots[step]
    
      ax.scatter(test_x, test_y, label='test', color='red')
      ax.plot(test_x, self.model.predict(test_x), label='prediction')
      ax.legend(['Test', 'Prediction'])

      ax.set_xticks(np.arange(-8, 10, 2))
      ax.set_yticks([])
      self.fig.add_subplot(ax)

class LossPlotCallback(tf.keras.callbacks.Callback):
  def __init__(self, steps = 5, epochs_step=10):
    super(LossPlotCallback, self).__init__()
    self.epochs_step = epochs_step

    rows = (steps + 4) // 5
    cols = 5
    self.fig = plt.figure(figsize=(20, rows * 2))
    self.fig.suptitle('Loss', fontsize=20, color='forestgreen')
    
    self.plots = self.fig.subplots(rows, cols).flatten()

  def on_train_begin(self,logs={}):
      self.losses = []
  
  def on_epoch_end(self, epoch, logs={}):
    self.losses.append(logs.get('loss'))
    mark = self.epochs_step - 1
    if epoch > 0 and epoch % mark == 0:
      step = epoch // mark - 1
      ax = self.plots[step]
    
      ax.plot(np.arange(len(self.losses)), self.losses, label='loss', color='orange')
      ax.legend(['Loss'])

      ax.set_xticks(np.arange(0, len(self.losses), 5 * (step + 1)))
      ax.set_yticks([])
      self.fig.add_subplot(ax)


