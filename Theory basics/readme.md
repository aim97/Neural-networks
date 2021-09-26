# Neural Networks

The concept of neural networks has been around for a many years, but it only start to shine in the past few decades thanks to the availability of enough computing resources to support it at affordable prices specifically referring to GPUs.

In this section we go over the intuition of neural networks, what they can help with, and the general process of training a neural network.

1. Intelligence
2. Artificial Intelligence
3. Neural Networks
4. General process of training a neural network

## Intelligence

It's a word we use frequenctly to describe an act, a choice or a disicion that yielded an outcome of interest to the one who made it, there are multiple definitions of intelligence but let's just stick with this one for now. for example when you make a choice to sell your stocks then right the next day the their prices go down, someone would say you had an insight into how the market was going and based on your observation you predicted such outcome and acted upon it, this is an intelligent behaviour based on our definition above.  

The way we see it here, is that intelligence is a logical action, you get observations, you predict what will happen, and based on the prediction you choose an action that maximizes your best interest, and you know what we love about logic, it's that no one can disagree with it, it has certain rules and you simply follow them to reach an answer, and you know who is also good at following rules, sure they are computers.

Computers are good at following steps and rules, and so by describing the rules and steps a human would carry out to reach and "intelligent" decision, a computer can follow those rules to reach the same disicion. at first we would explain what we do as algorithms and simply have the computer follow them, that's why introduction courses to AI usually start with search techniques like dfs and hill climbing, they are simply algorithms to search for best decision that maximizes a certain performance metric. then we reach what i consider as the end of the road for this kind on techniques when the inference engine was made.

Inference engines are simply programs to carry out logical inference, something like if *Ahmed said he will go play ball*, and *The only ball game Ahmed plays is football* then *Ahmed will play football*, it processes previous knowledge to reach new knowledge that would then be added to its knowledge. inference engines are the core of expert systems. in order to build an expert system, you first need to specify what kind of experience you want it to acquire, then gather a group of people who specialize in that field and have them write all that they know no matter how trivial in the form of rules (if possible), then the next step is to get an inference engine whose only job is to reason about those rules and answer specified queries. expert systems are great, they took us to the moon, they were used in business, games, ... etc, they can do a lot. one of the greatest feautes about them is their ability to provide steps and reasons for their choices making undertanding them easier, and it sure is a great help for debugging when you can see exactly what went wrong and why, but it's not much of a help, and we will know why very soon.  

As great as expert systems might be they have their own limitations, as you may have guessed, building the knowledge based with the cooperation of multiple professionals, is not as easy task, and even small mistakes can't be tolerated, even the text books we have to study from may include mistakes, but it doesn't affect humans much, for a computer however this can be fatal, for example if the knowledge base has two contradicting rules, or data, which will the inference engine follow. what if not all knowledge was added, usually something may be forgotten, how will the system work then, building a knowledge base is a lot of work.

Another big problem for expert system is their rigidity, the system is based on logic, even when it added probability to its judegements it still didn't completely solve the problem, improvements in expert systems became very hard as time went on. and they don't reach the desired performance for humanly simple tasks, like object detection, classification, ... etc, and as time went on they became obsolete.

## Neural networks

They rised to work where expert systems had failed, the main problems with expert systems were

1. They are hard to develop and maintain.
2. They need a knowledge base.

Expert systems are based entirely on the ability of humans to collect their knowledge into a knowledge base that the inference engine can reason about, but for a problem like object detection, to which humans can't write a a set of rules to solve it, or at least not enough rules to cover all cases, it inference engine won't be able to reach the required results, and leaves us with no choice but to search elsewhere for a solution.

If we think about it, An expert system is a way to describe intelligence as we know it, it simply simulates the process of making an intelligent decisions based on observations, and knowledge, but this approach have failed us. so how can we make a model that have an intelligent behaviour now?, brain is the part of our body that is responsible for control, and making decisions, and all approaches we made were to simulate its behaviour, but the expert system, while it have sucesseded in inference part of intelligence, it seems intelligence is not just inference, and so it couldn't reach the results we wanted.

Trying to simualte the brain behaviour, requires to understand every part of our human life, the choices of the brain and find some kind of reasons for them, then build a model that has the same behaviour, some of which are emotional and simply irrational. you can't build a logical model of something that is by definition is irrational.  

So instead of trying to build a model that simulates the brain high level behaviour (decision making, identifying objects, emotion recognition, localization, landmark detection), we will build a model that simulates the brain itself (the interaction between neurons and neurons them selves), since the brain is responsible for doing all those tasks, making something similar to it, should help us perform those tasks as well, and that's how the idea of neural networks came to life.

## Human brain

Before we start with building our artifical brain, we need to understand the structure of the real thing, and how it works.

<!-- TODO add more content here
1. image of nerve cells
2. explain how it works
 -->

## what is a Neural Network

it's the idea of simulating human level intelligence by using a model that follows the neural structure or human nerves and how they interact with one another, as well as the surrounding environment. A neural network is basically a connection of neurons, organized in layers, unlike normal AI methods where you have to know how to solve the problem in order to get it solved that 's to find an algorithm, a set of steps that you can follow in order to reach the solution, neural networks are used to learn those steps on their own from collected data.  

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

it's the most simple form of a neural network, just one nerve.  

### Human nervous system

The human nervous system is composed of a number of nerves, nerves have multiple types, but they have a general form:  

1. 


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