import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from math import floor


class PlottingCallback:
  def __init__(self, epochs_step, steps, title):
    super(PlottingCallback, self).__init__()
    self.epochs_step = epochs_step
    self.steps = steps

    rows = (steps + 4) // 5
    cols = 5

    self.fig, self.plots = plt.subplots(rows, cols, figsize=(17, rows * 3))
    self.fig.suptitle(title, fontsize=15, color='forestgreen')
    self.fig.tight_layout(pad=3.0)

    self.plots = self.plots.flatten()

class TestingPlotCallback(PlottingCallback, tf.keras.callbacks.Callback):
  def __init__(self, steps = 5, epochs_step=10, test_data=None):
    super(TestingPlotCallback, self).__init__(epochs_step, steps, "Testing")
    
    self.test_data = test_data

    y_min, y_max = min(test_data[1])[0], max(test_data[1])[0]
    yspread = y_max - y_min
    x_min, x_max = min(test_data[0])[0], max(test_data[0])[0]
    xspread = x_max - x_min
    

    self.lims = {
      "x": (
        floor(x_min - xspread * 0.1), 
        floor(x_max + xspread * 0.1), 
        floor(xspread * 1.2 // 5)
      ),
      "y": (
        floor(y_min - 0.1 * yspread),
        floor(y_max + 0.1 * yspread),
        floor(yspread * 1.2 // 5)
      )
    }

  def on_epoch_end(self, epoch, logs={}):
    mark = self.epochs_step - 1
    if epoch > 0 and (epoch + 1) % self.epochs_step == 0:
      step = epoch // mark - 1
      test_x, test_y = self.test_data
      ax = self.plots[step]
    
      ax.scatter(test_x, test_y, label='test', color='red')
      ax.plot(test_x, self.model.predict(test_x), label='prediction', color='blue')
      ax.legend(['Test', 'Pred'])
      ax.set_title(f'Epoch: {epoch + 1}')

      y_min, y_max, y_step = self.lims["y"]
      ax.set_xticks(np.arange(*(self.lims['x'])))
      ax.set_yticks(np.arange(y_min, y_max, y_step))
      self.fig.add_subplot(ax)

class LossPlotCallback(PlottingCallback, tf.keras.callbacks.Callback):
  def __init__(self, steps = 5, epochs_step=10):
    super(LossPlotCallback, self).__init__(epochs_step, steps, "Loss")

  def on_train_begin(self,logs={}):
      self.losses = []
  
  def on_epoch_end(self, epoch, logs={}):
    self.losses.append(logs.get('loss'))
    mark = self.epochs_step - 1
    if epoch > 0 and (epoch + 1) % self.epochs_step == 0:
      step = epoch // mark - 1
      ax = self.plots[step]
    
      ax.plot(np.arange(len(self.losses)), self.losses, label='loss', color='orange')
      ax.legend(['Loss'])
      ax.set_title(f'Epoch: {epoch + 1}')

      ax.set_xticks(np.arange(0, len(self.losses), 5 * (step + 1)))
      ax.set_ylim(0, max(self.losses) * 1.1)
      self.fig.add_subplot(ax)


