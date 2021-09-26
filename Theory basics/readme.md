# Neural Networks

The concept of neural networks has been around for a many years, but it only start to shine in the past few decades thanks to the availability of enough computing resources to support it at affordable prices specifically referring to GPUs.

In this section we go over the intuition of neural networks, what they can help with, and the general process of training a neural network.

## Intelligence

It's a word we use frequenctly to describe an act, a choice or a disicion that yielded an outcome of interest to the one who made it, there are multiple definitions of intelligence but let's just stick with this one for now. for example when you make a choice to sell your stocks then right the next day the their prices go down, someone would say you had an insight into how the market was going and based on your observation you predicted such outcome and acted upon it, this is an intelligent behaviour based on our definition above.  

The way we see it here, is that intelligence is a logical action, you get observations, you predict what will happen, and based on the prediction you choose an action that maximizes your best interest, and you know what we love about logic, it's that no one can disagree with it, it has certain rules and you simply follow them to reach an answer, and you know who is also good at following rules, sure they are computers.

Computers are good at following steps and rules, and so by describing the rules and steps a human would carry out to reach and "intelligent" decision, a computer can follow those rules to reach the same disicion. at first we would explain what we do as algorithms and simply have the computer follow them, that's why introduction courses to AI usually start with search techniques like dfs and hill climbing, they are simply algorithms to search for best decision that maximizes a certain performance metric. then we reach what i consider as the end of the road for this kind on techniques when the inference engine was made.

### Expert systems

<!-- TODO Add an image for expert systems -->

Inference engines are simply programs to carry out logical inference, something like if *Ahmed said he will go play ball*, and *The only ball game Ahmed plays is football* then *Ahmed will play football*, it processes previous knowledge to reach new knowledge that would then be added to its knowledge. inference engines are the core of expert systems. in order to build an expert system, you first need to specify what kind of experience you want it to acquire, then gather a group of people who specialize in that field and have them write all that they know no matter how trivial in the form of rules (if possible), then the next step is to get an inference engine whose only job is to reason about those rules and answer specified queries. expert systems are great, they took us to the moon, they were used in business, games, ... etc, they can do a lot. one of the greatest feautes about them is their ability to provide steps and reasons for their choices making undertanding them easier, and it sure is a great help for debugging when you can see exactly what went wrong and why, but it's not much of a help, and we will know why very soon.  

As great as expert systems might be they have their own limitations, as you may have guessed, building the knowledge based with the cooperation of multiple professionals, is not as easy task, and even small mistakes can't be tolerated, even the text books we have to study from may include mistakes, but it doesn't affect humans much, for a computer however this can be fatal, for example if the knowledge base has two contradicting rules, or data, which will the inference engine follow. what if not all knowledge was added, usually something may be forgotten, how will the system work then, building a knowledge base is a lot of work.

Another big problem for expert system is their rigidity, the system is based on logic, even when it added probability to its judegements it still didn't completely solve the problem, improvements in expert systems became very hard as time went on. and they don't reach the desired performance for humanly simple tasks, like object detection, classification, ... etc, and as time went on they became obsolete.

### Why Neural networks

Neural networks rose to power when expert systems have failed, the main problems with expert systems were

<!-- TODO recheck the fallbacks of expert systems -->
1. They are hard to develop and maintain.
2. They need a knowledge base.

Expert systems are based entirely on the ability of humans to collect their knowledge into a knowledge base that the inference engine can reason about, but for a problem like object detection, to which humans can't write a a set of rules to solve it, or at least not enough rules to cover all cases, the inference engine won't be able to reach the required results, and leaves us with no choice but to search elsewhere for a solution.

If we think about it, An expert system is a way to describe intelligence as we know it, it simply simulates the process of making an intelligent decisions based on observations, and knowledge, but this approach have failed us. so how can we make a model that have an intelligent behaviour now?, brain is the part of our body that is responsible for control, and making decisions, and all approaches we made were to simulate its behaviour, but the expert system, while it have sucesseded in inference part of intelligence, it seems intelligence is not just inference, and so it couldn't reach the results we wanted.

Trying to simualte the brain behaviour, requires to understand every part of our human life, the choices of the brain and find some kind of reasons for them, then build a model that has the same behaviour, some of which are emotional and simply irrational. you can't build a logical model of something that by definition is irrational.  

So instead of trying to build a model that simulates the brain high level behaviour (decision making, identifying objects, emotion recognition, localization, landmark detection), we will build a model that simulates the brain itself (the interaction between neurons and neurons them selves), since the brain is responsible for doing all those tasks, making something similar to it, should help us perform those tasks as well, and that's how the idea of neural networks came to life.

### Human brain

Before we start with building our artifical brain, we need to understand the structure of the real thing, and how it works.

<!-- TODO add more content here
1. image of nerve cells
2. explain how it works
 -->

## Neural Network

<!-- TODO add an image of a single perceptron -->

Now, what we want is a mathematical model that works in approximately the same way a neuron cell would. we saw that each input to the neural network is processed individually, then the results are merged together to create the required output.  

Then we can model the neuron as

```math
Merge(F1(I1), F2(I1), F3(I3), ..., Fi(Ii), ... , Fn(in))
```

where

1. **n** is the number of inputs.
2. **Ii** and **Fi** are the ith input and the function applied to it respectively.  
3. **Merge**: the function that merges the them.

This seems about right, but we have a problem, we don't know what functions the actual neuron use, and that's too many functions for the simplest intelligent unit, so we will assume that those functions are simply linear functions.

so `Fi(Ii) = Wi*Ii` where `Wi` is a parameter for the linear function, now then we need to merge those results, so we will use simple addition to do that, and add a bias term `b` to complete the linear functions we have, since the bias is just a constant we will add it only once in the merge function.

let `Z` be the output of the merge function:

```math
Z = F1(I1) + F2(I2) + F3(I3) + ... + Fn(In) + b = sum(i=1, n, Fi(Ii)) + b = sum(i=1, n, Wi * Ii) + b
```

and with this we got ourselves a model that we can work with, which we will call a **perceptron**, we can connect it to other perceptrons and form the neural network we have been talking about all this time, except not just yet, we had problems with the previous model since we didn't know what functions are used, and even after assuming they were linear now, what are the correct values of `w` and `b`, after all we can only compute the value of the output `z` after *learning* `w` and `b`.

We have to agree what we did just now is making a model that should simulate the brain, but it is not working yet, the inference engine needed a knowledge-base (data and rules about the problem it's trying to solve) in order to reach an answer, every algorithm you write have to have some rules embedded in it related to the problem it's trying to solve, but there is no knowledge base here, or to be more accurate, we are simulating the entire brain and the knowledge base should be there somewhere.

### How we learn

You can think of the state our model is in right now as a new born baby, he knows nothing about his environment or what kind of problem his parents got him into, only by living a experiencing various things can he understand. and now we know what our model needs is a way to learn the problem it should solve and what kind of solution it's expected to reach, that last part is important since we don't want another AI giving us a `42`.  

### Teaching AI agents

<!-- TODO add an image of a neural network -->

In order to teach a human you need to specify

1. Target: what are the intended learning outcomes he should learn.
2. Data: the content you want him to learn, which should conform with the target.
3. A performance measure: someway to measure how much did he learn, a way to assess his performance, like exams, and assignments.
4. a Teacher: to guide the student during his learning process.

As long as the student didn't reach a satisfactory result in the performance measure, the Teacher will keep helping the student to reach the target skill level. And we will basically have to provide those to the AI agent, and make it follow a similar learning cycle, and The expected outcome for teaching/training a neural network is the correct values of `w` and `b` the parameters of the model.  

We can think of a neural network as a complicated function, in that since:

1. The data the model will learn is numeric data which will act as an input to the function.
2. The performance measure (from here onwards called a cost function) should be a function that calculates the difference between the expected output and the value computed by the model.
3. The teacher is an optimization algorithm, that updates the values of `w` and `b` to reduce the Cost function.

The cycle of learing here comes in 3 steps

1. The model is given a set input data, and is expected to given an output for them.
2. The Cost function computes the difference between the model output and correct output.
3. The optimizer updates the weights and bias to reach lower cost function, and repeat from step `1`.

So the components of the process fall down to `dataset`, `cost-function` and `optimizer`, and how each of them works is a topic on its own, what you need to know for now is that once the model is trained, you will have working values from `w` (from here onwards refered to as weights) and `b` (from here onwards refered to as bias), you can give input to the model and get the expected  output.

### Activation function

<!-- TODO add more images here for activation functions -->

Our model is now fine but it has something missing, as it's now the output our model is giving is a continous function, specifically a linear function, soon we will prove that using a linear function makes adding multiple layers (feeding the output of one perceptron an input to another and so on) add no value.  

Mostly our outputs is categorical not continuous, for example, the famous problem of *breast cancer recognition* task, given an image the model, should classify it as either `malignant` or `benign`, this is called a *binary classification* problem, since we classify into 2 classes, a value that can range from `-inf` to `inf` wouldn't be of much help in when we have two classes.  

That's why we will add more complexity to our model by adding non-linearity to the merge function, instead of returning `z` we will return  *&sigma;(z)* where *&sigma;* is a non-linear function, there are multiple non-linear functions, like `tanh`, `sigmoid`, `relu`, `linear` ... etc. for the time being we will stick with either `linear` as we did so far or choose `sigmoid` and we will explain the differences in the next module.

## What next

This module covered the components of the model training process, without going into details into any of them, so it's natural if you feel like you didn't understand the concept yet, this is the big picture, you may want to re-read this module after going further into this tutorial to gain the most from it, from this point we will go through the whole process of training a model using the standard path

- [ ] How to build the structure of neural net. (single neuron, a layer, then multi layer model).  
- [ ] Mean square root loss (Loss function and Cost function).  
- [ ] Back-propagation (Stochastic Gradient Discent Optimizer).  
- [ ] Linear regression.

After understanding this path, the rest is just a matter of replacing one component with another to do the same job just in a better way, with no change to other parts.
