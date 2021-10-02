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
  - [x] [Sequential model - notebook](./Tensorflow-what-you-need-to-know.ipynb):  it covers the most basic use of Tensorflow, through the Sequential model.  
  - [x] [Functional API 1 - notebook](./FunctionalAPI-1.ipynb): it demonstrates the use of Tensorflow functional API, which can be used to build more complex models, it works on energy + effciency dataset.
  - [x] [Functional API 2 - notebook](./FunctionalAPI-2.ipynb): it demonstrates the use of Tensorflow functional API, which can be used to build more complex models.
  - [ ] What is a tensor?
  - [x] [Customization: custom layer - notebook](./custom-layer.ipynb): it demonstrates how to create a custom layer in Tensorflow.
  - [x] [Customization: custom loss - notebook](./custom-loss.ipynb): it demonstrates how to create a custom loss in Tensorflow.
  - [x] [Customization: custom model](./custom_model.ipynb): it demonstrates how to create a custom model in Tensorflow, using `Resnet18` and `VGG16` as examples.
  - [ ] Customization: custom optimizer - notebook
  - [ ] Notes and remarks

- CNN
  - [ ] Convolutional network
  - [x] ResNet
    - [x] Residual network architecture
    - [x] The results obtained from the ResNet paper
    - [x] Tensorflow Resnet
  - [ ] Inception network
  - [ ] Object detection: YOLO and the gang
  - [ ] Summary
