
Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     


.. image:: images/aws_logo.png
   :target: images/aws_logo.png
   :alt: 


Lab 3:  

HPO for SciKit Learn on SageMaker
=================================

Step 1
------

Introduction

Hyperparameter tuning is a supervised machine learning regression problem. Given a set of input features (the hyperparameters), hyperparameter tuning optimizes a model for the metric that you choose. You can choose any metric that the algorithm you use defines. To solve a regression problem, hyperparameter tuning makes guesses about which hyperparameter combinations are likely to get the best results, and runs training jobs to test these guesses. After testing the first set of hyperparameter values, hyperparameter tuning uses regression to choose the next set of hyperparameter values to test.

Step 2
------

Creating our HPO Job


#. 
   Select the 03_HPO_with_SciPi.ipynb notebook


   .. image:: images/lab2/pic1.png
      :target: images/lab2/pic1.png
      :alt: 


#. 
   Let's look at the notebook We'll setup the same dataset and Estimator as before  

   Normally you'll have these defined once in a single notebook or python file but we define it again here to be explicit and for readers to see exactly what needs to be defined.  

   Run the first cell that defines the role

#. 
   Just as before, let's setup the dataset used for each of the training jobs that our HPO will kick off


   .. image:: images/lab2/pic2.png
      :target: images/lab2/pic2.png
      :alt: 


#. 
   The next cell defines a few critical things:


   * 
     The estimator that each job will use, we are using scikit


     .. image:: images/lab2/pic3.png
        :target: images/lab2/pic3.png
        :alt: 


   * 
     The Hypterpameter range that our HPO job should use as it kicks off various jobs:


     .. image:: images/lab2/pic4.png
        :target: images/lab2/pic4.png
        :alt: 


   * 
     Finally, our objective metric, which tells us how well the model performs, and how many parrallel and total jobs to run


     .. image:: images/lab2/pic5.png
        :target: images/lab2/pic5.png
        :alt: 


  The last part of this cell, which you should go ahead and execute, starts the HPO job:

  
.. image:: images/lab2/pic6.png
   :target: images/lab2/pic6.png
   :alt: 



#. 
   Kick off the job, you should see a message that it's saying it's starting:


   .. image:: images/lab2/pic7.png
      :target: images/lab2/pic7.png
      :alt: 


Step 3
------

Evaluting the HPO Job


#. 
   Let's see how we can pull the tuning job name into the parameter and wait for it to finish now in the next two cells:


   .. image:: images/lab2/pic8.png
      :target: images/lab2/pic8.png
      :alt: 


#. 
   We can start analyzing the results of the jobs:


   .. image:: images/lab2/pic9.png
      :target: images/lab2/pic9.png
      :alt: 


#. 
   First lets look at our training objective score over time


   .. image:: images/lab2/pic10.png
      :target: images/lab2/pic10.png
      :alt: 


#. 
   Now let's look per objective, the training objective


   .. image:: images/lab2/pic11.png
      :target: images/lab2/pic11.png
      :alt: 



   .. image:: images/lab2/pic12.png
      :target: images/lab2/pic12.png
      :alt: 



   .. image:: images/lab2/pic13.png
      :target: images/lab2/pic13.png
      :alt: 


© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
