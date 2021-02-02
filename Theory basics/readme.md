# Neural Networks

The concept of neural networks has been around for a many years, but it only start to shine in the past few decades thanks to the availability of enough computing resources to support it at affordable prices specifically referring to GPUs.

In this section we go over the intuition of neural networks, and why do we need them.  
Then our first neural network or actually just a single *perceptron*
Then how we get this neural network to *learn* and how we use it after wards.
And finally some examples of problems that neural network can help with.

## what is a Neural Network

it's the idea of simulating human level intelligence by using a model that follows the neural structure or 
human nerves and how they interact with one another, as well as the surrounding environment.
A neural network is basically a connection of neurons, organized in layers, unlike normal AI methods where
you have to know how to solve the problem in order to get it solved that 's to find an algorithm, a set of 
steps that you can follow in order to reach the solution, neural networks are used to learn those steps on 
their own from collected data.  

for a neural network to work, it needs to be *trained*, as we said the idea of neural networks is to make an
intelligent system that can learn through training, just like humans do, you need to train on a certain
problem like solving quadratic equation in order to get it right easily and faster, the element of training
is more evident in terms of experience, those who work on a certain field for a long time develop some
*intuition* about how to address problems in that field, and gain *sense* about what the right solution is,
this sense or intuition is what we call as learning and this is what we want the neural network to follow,
we want the neural network model to gain the ability to learn from example data on its own, most if not all 
the time the process of algorithm design is painful, it takes a lot of time to design the algorithm, test and
show that it actually works and why it does, as problems become complicated we may not be able to write 
certain steps or conditions based on which the computer can build its reasoning scheme, most of these problems 
are humanly intuitive like object recognition, or voice recognition, as a human you don't follow steps in 
order to do those tasks you simply get the answer just like that, you know a cat when you see one, this is 
not a challenge for human intelligence, this is the power of *intuition*, and this particular human 
characteristic is what we want a neural network to exhibit.  

to summarise this: building a neural network is all about building the intuition to reason about some problem,
this is done by training the neural networks on previously collected data, iteratively until it reaches a 
sufficient performance level, then it's ready to work, that is we can feed unanswered questions to the neural 
net and it should provide an answer, this is the general idea, how to build a neural nets and its components, 
how the training occurs, how we use the neural network afterwards and what kind of problems we expect a neural
network to solve is something we will get to shortly, but first let's discuss our very first and simlest neural network, *the perceptron*.

## Perceptron

it's the most simple form of a neural network, just one nerve,
**How does a Perceptron work?**
like a nerve in your body a perceptron receives input signals, treats each of them based on their value, and
computes a function, if the value of the neuron is beyond a certain limit it fires otherwise it doesn't 

## learning process

### components learning process

#### model

this is the neural network structure of all layers and neurons in it.

#### Cost function

it's a function that call tell how good or bad the neural network is doing by comparing the neural network output to the expected output

#### Optimizer


There are many types of problems neural networks are used for the most dominant of which are  

## The problems that can be solved by Neural-Nets.

### Regression

a Regression problem is one in which the output has a continuous distribution rather than a discrete one, 
like the prediction of stock prices based on their previous values.  
it's not quite likely to use a neural net for this

### Classification

it's a problem where you need to classify a certain object to one or more classes, like object recognition.