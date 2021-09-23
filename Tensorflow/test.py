from simple_model import train_model
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def Huber_loss(threshold) -> tf.keras.losses.Loss:

  @tf.function
  def huber_loss(y_true, y_pred):
    """Calculates the huber loss.
    Parameters
    ----------
    y_true : tensor of true targets.
    y_pred : tensor of predicted targets.

    Returns
    -------
    loss : tensor, shape (batch_size, 1)
    """
    err = y_true - y_pred

    cond = tf.abs(err) < threshold
    L2 = 0.5 * tf.square(err)
    L1 = tf.abs(err) - 0.5
    loss = tf.where(cond, L2, L1)   # Keras does not cover where function in tensorflow :-(

    return loss
  
  return huber_loss

# lets create some basic setup to test the huber loss
# we will use a simple linear regression model
# with a huber loss
x = np.linspace(-10, 10, 100)
y = 2 * x + 7 + np.random.normal(0, 0.1, 100)

test_x = np.random.uniform(-10, 10, 20).reshape(-1, 1)
test_y = 2 * test_x + 7


train_model(Huber_loss(0.5), x, y, test_x, test_y, epochs_step=20, steps = 10)

plt.show()