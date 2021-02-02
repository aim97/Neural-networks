# Structuring Machine Learning Projects
This section will discuss the process of building a Deep learning model, the steps you need to take through out the development, and how to solve the problems that arise in during it in the most effective way.  
This Section is based on the Deeplearning.ai course with same name, and is made to summarize and focus its content.

### Why?
The process of building a Deep learning model can be quite lengthy, when you reach a low accuracy there are many  things you might want to try, like getting more data, adjusting the hyper parameters (learning rate, B.N. beta, ...etc), changing the optimization technique, or using a whole new neural network architecture.  

All these solutions are great but which one is most effective?, you may spend months collecting more data only to get slight increase in accuracy, only to realize afterwards that you could solve the problem by adding more layers, or using a new network architecture could have solved your problem faster.

This section is like guidelines and best practices to take to develop Deep learning models faster.

### ILOs
After completing this section you should be able to answer the following questions about your ML project.
1. If the performance is low, what is the problem?
2. How to best address the problem while avoiding any unintended effects on other metrics?


## Orthogonalization
It's the act of isolating the effects of your actions, to make sure no unintended conequences would arise, for example, *Batch normalization* is an action that **ONLy**  affects *variance*, *adding more data* is an action that should **ONLY** affect *avoidable-bias*.
### Why use Orthogonalization?
it makes results easier to understand, and makes decision making easier, when ever you find a problem during
the development, you first identify the problem, is it *bias*, *variance*, *both*, *mismatch issue*, ...etc.  

once the problem is known you only try the set of methods the affect the variable that has a problem, 
if you don't use orthogonalization, then whenever you try to solve one variable you may end up missing with
another one, and getting into a lengthy development cycles to tune everything together at the same time.  

However once you make sure that the methods you use only affect one variable, then you can tune each of them 
independently which is much easier.

Actually, one of the techniques that affect more than one variable is **Early stopping**, it affects the training 
as well as the validation accuracy, that's why it's not prefered.

## Steps of Deep learning model development
your priorities are as listed below in order:
1. Improve your performance on training set as much as possible.
    . Another optimizer
    . Bigger network
    . ...etc 
2. Improve your performance on validation set
    . Regularization technique 
    . More data
3. Improve your performance on testing set
    . Make dev-set bigger -> to prevent over-fitting to the dev-set
4. Improve your performance for real world problems.
    . Changing the cost function
    . Changing the dev-set

## Single Number Evaluation metrics
Mostly in Machine learning applications the metrics of performance aren't just the accuracy, there is also
time performance, the memory required, Precision and recall, there may be even more metrics depending on
what you want the final system to look like.

In such case, when you are trying multiple models, how can you tell which is better?, if one has low accuracy but 
the model size is significantly small while another model is large but gives a very high accuracy, how can you 
judge which model is **"better"**?.

The answer is simple, you need to define what **"better"** means, in a sense, what you need is an *evaluation function*
that given a model would output a single number representing the *fitness value* of that model.    

### Precision and recall
they are evaluation metrics for classification problems  
**Precision:** for any class A, it's the percentage ratio between correctly classified samples of that class
and the number of samples classified as class A.  
in other words, out of all samples that were classified as A, how many were correct?   
```
(correctly Classified samples) / (all classifications)
```

**Recall:** for any class A, it's the percentage ratio between correctly classified samples of that class 
and the number of samples of that class in the dataset.  
in other words, out of all samples of class A in the validation set, how many were correctly classified?  
```
(correctly Classified asamples) / (all samples)
```

##### F1 score
- it's the standard way to combine *Precision* and *Recall*, 
- it's the harmonic mean of *Precision* and *Recall*
```
F1_score = 2 / (1/P + 1/R)
```
where *P* is Precision and *R* is recall.

### Satisficing and optimizing parameters
there are 2 different type of metrics of performance of a model in terms of how they are enforced on the model  
**Satisficing parameters**: they are parameters that are under range constraints, using thresholds, for example
the execution time must be less than 1 sec, unless the model satisfies this criterion, it's rejected.

**Optimizing parameters**: they are parameters subject to optimization (minimization, maximization, ... ect), 
like accuracy, the higher the accuracy the better, regardless of the accuracy value as long as it's the highest
the model would be a candidate to be chosen.  

***P.S.***: i think the naming should be *Satisficing and optimizing constraints*, since a parameter like the
execution time can also be subject to optimization, you sure want to minimize the execution time as much as 
possible, it just doesn't feel urgent as long as you pass a certain threshold, but you can still include it
for optimization in case the application is time-critical, and something like accuracy can be subject to satisficing
constraints, you may not want to accept a model if its accuracy is below a certain level, even if it's the best you could 
reach.  

### Single Evaluation metric: How to?
Most of the time you would try to place the satisficing constraints on all metrics of interest except the one you
want to optimize.

| Metric of performance | Sufficient level | Optimization |
|-----------------------|------------------|--------------|
| Execution time        | 1000 ms          | minimize     |
| Accuracy              | 98%              | maximize     |
| Model size            | 1 MB             | minimize     |

for the above scenario, we will need to work three times, optimize for execution time, while making sure that the 
Accuracy and Model size are within the allowed range, then we try to improve accuracy while making sure the other
two factors stay within the allowed range, and same with the Model size.

There is also another method that you can try to do the evaluation, it's to embed the all the metrics in the cost
function based on the way you want, however this method is complicated since you need to tune the relations between
the parameters when used in the same equation, the least example is using a linear combination, you would need
to tune the parameter of each of the metrics
```
cost = A * Accuracy + B * Time + C * memory 
```
you minimize the loss function and tune the parameters A, B, and C to the value that fits your priorities, this
process is complicated, adds more tuning, and requires better understanding of the relation between the parameters
to form a realistic cost function, so it's always better to use the first method to independently optimize the metrics 
we want.   

#### Notes

Suppose you are building a "Cat sharing" app, it allows users to share their cat images. you decided to use a classifier to check if the uploaded image is a cat or not before allowing it.

Which would you prefer a classifier with 99% accuracy that allows porn images, or another with 97% accuracy but doesn't allow porn images, you and your customers would prefer the second one since it prevent Porn more, but according your evaluation metrics the first is better. **when such a situation occurs, it means your evaluation metric is not right**, you need to re-think your evaluation matrics.

So how do we prevent our model from allowing Porn images?, in this simple case we can modify the cost function by adding a weight to the loss of each sample, if the miss-classified sample is normal the weight is just 1, when it's a Porn image the weight is a large number like 10, this way the model will be pushed to prioritize the prevention of Porn images.  

This fault occurred because the evaluation metric wasn't set correctly, those metrics are not just the problem definition, the metrics you create must really reflect the needs of your application, and the real working environment.
 
## Summary
1. Orthogonalization means that you use *one technique* to carry *one job* and affect only *one variable*.
2. Early stopping affects both training and testing accuracy.
