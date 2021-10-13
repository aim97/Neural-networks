# Neural network

- Deep learning
  - [ ] Basics of neural networks
    - [x] [intro](./Theory%20basics/readme.md): Introduction to neural networks along with some history.
    - [ ] Using the neural networks: Regression vs Classification.
    - [ ] Learning: it covers how the model training is done in general, and how backpropagation works.
    - [ ] Cost function
    - [ ] Optimization
  - [ ] Optimization and hyper parameters
    - [x] [Bias x Variance tradeoff](./Theory%20basics/Improving%20DNNs/biasVariance.md): How to choose the right hyper parameters for a given dataset.
    - [ ] Overfitting vs Regularization techniques
    - [x] [Machine learning strategy](./Theory%20basics/Improving%20DNNs/ML_strategy.md): discusses the process of training a model and the decisions taken through it, like hyperparameter tuning process, the idea of orthogonalization.

- Tensorflow
  - [x] [Sequential model - notebook](./Tensorflow/Tensorflow-what-you-need-to-know.ipynb):  it covers the most basic use of Tensorflow, through the Sequential model.  
  - [ ] [Model storage](./model-storage.ipynb): this module covers how to store a trained model and how to rebuild a model from its stored version.
  - [x] [Functional API 1 - notebook](./Tensorflow/FunctionalAPI-1.ipynb): it demonstrates the use of Tensorflow functional API, which can be used to build more complex models, it works on energy + effciency dataset.
  - [x] [Functional API 2 - notebook](./Tensorflow/FunctionalAPI-2.ipynb): it demonstrates the use of Tensorflow functional API, which can be used to build more complex models.
  - [x] [Customization: custom layer - notebook](./Tensorflow/custom-layer.ipynb): it demonstrates how to create a custom layer in Tensorflow.
  - [x] [Customization: custom loss - notebook](./Tensorflow/custom-loss.ipynb): it demonstrates how to create a custom loss in Tensorflow.
  - [ ] Metrics: it explains what metrics are, how to use built-in metrics, and how to build your own.
  - [x] [Customization: custom model](./Tensorflow/custom_model.ipynb): it demonstrates how to create a custom model in Tensorflow, using `Resnet18` and `VGG16` as examples.
  - [x] [Callbacks](./Tensorflow/callbacks.ipynb): it explains what callbacks are, how to use built-in callbacks, and how to build your own.
  - [ ] Customization: custom optimizer - notebook
  - [x] [What is a tensor?](./Tensorflow/tensors.ipynb): covers what tensor is, how to create it and use it.
  - [x] [Gradient Tape](./Tensorflow/gradient-tape.ipynb): it explains how to use the gradient tape to calculate gradients, as a step to customize the leasrning process.
  - [x] [custom training](./Tensorflow/custom-training.ipynb): it demonstrates how to create a custom training loop in Tensorflow, you may want to use that if you want to do training in an inconventional way, like using more than the first derivate.
  - [ ] Graph mode - notebook

- CNN
  - [ ] Convolutional network
  - [x] ResNet
    - [x] [Residual network architecture](./CNNs/ResNet/readme.md)
    - [x] [The results obtained from the ResNet paper](./CNNs/ResNet/ResNet-Results.md)
    - [x] [Tensorflow Resnet](CNNs/ResNet/tf-resnet.md)
  - [ ] Inception network
  - [ ] Object detection: YOLO and the gang
  - [ ] Summary
