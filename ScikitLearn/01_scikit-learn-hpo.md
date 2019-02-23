Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     

![](images/aws_logo.png)

Lab 3:  
HPO for SciKit Learn on SageMaker
============================================

Step 1
------

Introduction

Hyperparameter tuning is a supervised machine learning regression problem. Given a set of input features (the hyperparameters), hyperparameter tuning optimizes a model for the metric that you choose. You can choose any metric that the algorithm you use defines. To solve a regression problem, hyperparameter tuning makes guesses about which hyperparameter combinations are likely to get the best results, and runs training jobs to test these guesses. After testing the first set of hyperparameter values, hyperparameter tuning uses regression to choose the next set of hyperparameter values to test.

Step 2
------

Creating our HPO Job

1.  Select the 03\_HPO\_with\_SciPi.ipynb notebook

  ![](images/lab2/pic1.png)

2.  Let's look at the notebook We'll setup the same dataset and Estimator as before  

  Normally you'll have these defined once in a single notebook or python file but we define it again here to be explicit and for readers to see exactly what needs to be defined.  

  Run the first cell that defines the role
3.  Just as before, let's setup the dataset used for each of the training jobs that our HPO will kick off

  ![](images/lab2/pic2.png)

4.  The next cell defines a few critical things:

  *   The estimator that each job will use, we are using scikit

      ![](images/lab2/pic3.png)

  *   The Hypterpameter range that our HPO job should use as it kicks off various jobs:

      ![](images/lab2/pic4.png)

  *   Finally, our objective metric, which tells us how well the model performs, and how many parrallel and total jobs to run

      ![](images/lab2/pic5.png)


  The last part of this cell, which you should go ahead and execute, starts the HPO job:

  ![](images/lab2/pic6.png)

5.  Kick off the job, you should see a message that it's saying it's starting:

  ![](images/lab2/pic7.png)


Step 3
------

Evaluting the HPO Job

1.  Let's see how we can pull the tuning job name into the parameter and wait for it to finish now in the next two cells:

  ![](images/lab2/pic8.png)

2.  We can start analyzing the results of the jobs:

  ![](images/lab2/pic9.png)

3.  First lets look at our training objective score over time

  ![](images/lab2/pic10.png)

4.  Now let's look per objective, the training objective

  ![](images/lab2/pic11.png)

  ![](images/lab2/pic12.png)

  ![](images/lab2/pic13.png)


© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
