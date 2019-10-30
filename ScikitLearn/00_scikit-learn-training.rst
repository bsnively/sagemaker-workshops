.. role:: raw-html-m2r(raw)
   :format: html


  Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     


.. image:: images/aws_logo.png
   :target: images/aws_logo.png
   :alt: 


SciKit Learn on SageMaker
=========================

Step 1
------

Introduction

(from wikipedia) Scikit-learn is a free software machine learning library for the Python programming language.[3] It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.  

In this first section, we'll create a script that we can use within the SciKit Learn Estimator in SageMaker. `scikit learn SageMaker Estimator <https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/sklearn/README.rst#scikit-learn-estimators>`_

Step 2
------

Developing our Scikit Script


#. 
   Select the 01_DevelopingYourSciKitLearnScript.ipynb notebook


   .. image:: images/lab1/pic1.png
      :target: images/lab1/pic1.png
      :alt: 


#. 
   **Important**\ : We'll see that SageMaker uses arguments into your scripts to pass in the hyperparameters. We are going to test and simulate this now as we develop our script  

   This is what we'll see later in the logs of the SageMaker container:


   .. image:: images/lab1/pic2.png
      :target: images/lab1/pic2.png
      :alt: 


#. 
   Let's look at the notebook that we'll use to unit test our scikit script.  

   Run the first cell that sets up the same environment variables that the SageMaker container passes in:


   .. image:: images/lab1/pic3.png
      :target: images/lab1/pic3.png
      :alt: 


   These settings are used to tell the script where the data is being passed in as well as where to store the model.

#. 
   Run the next cell. This cell creates the directories and loads some test data as we develop our script.


   .. image:: images/lab1/pic4.png
      :target: images/lab1/pic4.png
      :alt: 


#. 
   Run the next cell. This actually tests our script\ :raw-html-m2r:`<br>`
   **NOTE:** This will fail since we need to add/fix the script some by adding some code. you should see the error below:


   .. image:: images/lab1/pic5.png
      :target: images/lab1/pic5.png
      :alt: 


Step 3
------

Writing the Scikit Script


#. We'll be using a decision tree classifier\ :raw-html-m2r:`<br>`
   `Decision Tree Classifier link <https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html>`_
#. 
   On the Notebook instance, navigate to the scikit_learn_your_mission.py file


   .. image:: images/lab1/pic6.png
      :target: images/lab1/pic6.png
      :alt: 


#. 
   First thing you'll notice is that we want to be able to use three hyperparamters passed in, but the code is only expecting 1. You're task is to read in the other 2 hyperparameters into the script:


   .. image:: images/lab1/pic7.png
      :target: images/lab1/pic7.png
      :alt: 


#. 
   After making that change, you'll notice if you re-run the script in the jupyter notebook, then you'll see a different error:


   .. image:: images/lab1/pic8.png
      :target: images/lab1/pic8.png
      :alt: 


#. 
   Let's now check and update where it needs those parameter set in the file:


   .. image:: images/lab1/pic9.png
      :target: images/lab1/pic9.png
      :alt: 


#. 
   After setting the variables correctly being passed to the classifier, you should see this:


   .. image:: images/lab1/pic10.png
      :target: images/lab1/pic10.png
      :alt: 


#. 
   Let's test reading in the model and inferring here before jumping to the SageMaker training  

   This next cell re-reads in the classifier and infers on teh training data (usually this would be a different dataset)


   .. image:: images/lab1/pic11.png
      :target: images/lab1/pic11.png
      :alt: 


Step 4
------

Scikit Learn Estimator training through SageMaker


#. 
   Next we'll launch into a different notebook that uses the SageMaker Scikit learn Estimator to train our model.  

   Launch the 02_TrainingInSageMaker.ipynb notebook


   .. image:: images/lab1/pic12.png
      :target: images/lab1/pic12.png
      :alt: 


#. 
   Run the first cell, this will setup the IAM role that the SageMaker uses to do the training  

   **NOTE:** it's important to keep this least priv in production


   .. image:: images/lab1/pic13.png
      :target: images/lab1/pic13.png
      :alt: 


#. 
   This next cell uploads the training data for the training job.\ :raw-html-m2r:`<br>`
   we see the location that the training containers will be passed printed at the end of the execution of this cell.


   .. image:: images/lab1/pic14.png
      :target: images/lab1/pic14.png
      :alt: 


#. 
   Next we'll create the Scikit Estimator. Notice we pass:\ :raw-html-m2r:`<br>`
   Script Location\ :raw-html-m2r:`<br>`
   Role/session info\ :raw-html-m2r:`<br>`
   Hyperparamters\ :raw-html-m2r:`<br>`
   Additional training instance size information


   .. image:: images/lab1/pic15.png
      :target: images/lab1/pic15.png
      :alt: 


#. 
   Running the next call actually triggers the training job via the "fit" call.  

   The parameters are passing in the "train" channel with the S3 location that we created and loaded the dataset to earlier.


   .. image:: images/lab1/pic16a.png
      :target: images/lab1/pic16a.png
      :alt: 


   As it's training, you'll also notice the training job executing if you go to the SageMaker console under Training Jobs:


   .. image:: images/lab1/pic16b.png
      :target: images/lab1/pic16b.png
      :alt: 


   You'll also notice the script gets executed the same way passing in the hyperparameters as the notebook we were testing with before:


   .. image:: images/lab1/pic16c.png
      :target: images/lab1/pic16c.png
      :alt: 


Step 5
------

Testing the Model Locally


#. 
   Since we just built a model, we can see where the job stored it as well as the training job name:


   .. image:: images/lab1/pic17.png
      :target: images/lab1/pic17.png
      :alt: 


#. 
   Next, we'll download the model locally, and unpack it, load the classifier


   .. image:: images/lab1/pic18.png
      :target: images/lab1/pic18.png
      :alt: 


#. 
   Test some inferencing....


   .. image:: images/lab1/pic19.png
      :target: images/lab1/pic19.png
      :alt: 


© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
