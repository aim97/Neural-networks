# Improving Deep Neural Networks: Hyper-parameter tuning, Regularization and Optimization
This section is dedicated to possible improvements to *Deep neural nets*, how to find the best hyper parameters? how to improve the training error, while preventing over-fitting, increase the training speed and more.    

## Overview
the targets of this section are
1. make neural network learn faster (need less epochs to converge)
2. make neural network learn better (reaches higher training accuracy)
3. prevent neural network from over-fitting

### How to achieve faster training
A. use a better optimizer, the optimizer is the one responsible for **updating the neural network weight**, so it's the one responsible for the neural network reaching the target (minimum loss), reaching it fast, reaching it eventually or never reaching it at all.

Many optimization techniques are available, among them the mostt common are the following

1. Stochastic Gradient Descent
2. Mini-batch Gradient Descent.
3. Momentum Gradient Descent
4. Root Mean Square Prop
5. Adam Optimizer

there are other optimizers in tensorflow and you can also create custom optimizers in and pass them for you model to use.

<!-- 
### How to improve the network accuracy


### How to prevent Over-fitting 
1. Regularization parameters
2. Normalization
3. Early stopping
4. Dropout layers
5. Maxout networks

it's also worth mentioning that the following techniques also have a regularization effect.

 ### content
 1. Hyper parameter tuning
 2. Regularization
 3. Optimizers
 
  -->