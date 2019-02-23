  Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     

![](images/aws_logo.png)

SciKit Learn on SageMaker
====================================

Step 1
------

Introduction

(from wikipedia) Scikit-learn is a free software machine learning library for the Python programming language.\[3\] It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.  

In this first section, we'll create a script that we can use within the SciKit Learn Estimator in SageMaker. [scikit learn SageMaker Estimator](https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/sklearn/README.rst#scikit-learn-estimators)

Step 2
------

Developing our Scikit Script

1.  Select the 01\_DevelopingYourSciKitLearnScript.ipynb notebook

    ![](images/lab1/pic1.png)

2.  **Important**: We'll see that SageMaker uses arguments into your scripts to pass in the hyperparameters. We are going to test and simulate this now as we develop our script  

    This is what we'll see later in the logs of the SageMaker container:

    ![](images/lab1/pic2.png)

3.  Let's look at the notebook that we'll use to unit test our scikit script.  

    Run the first cell that sets up the same environment variables that the SageMaker container passes in:

    ![](images/lab1/pic3.png)

    These settings are used to tell the script where the data is being passed in as well as where to store the model.
4.  Run the next cell. This cell creates the directories and loads some test data as we develop our script.

    ![](images/lab1/pic4.png)

5.  Run the next cell. This actually tests our script  
    **NOTE:** This will fail since we need to add/fix the script some by adding some code. you should see the error below:

    ![](images/lab1/pic5.png)


Step 3
------

Writing the Scikit Script

1.  We'll be using a decision tree classifier  
    [Decision Tree Classifier link](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
2.  On the Notebook instance, navigate to the scikit\_learn\_your\_mission.py file

    ![](images/lab1/pic6.png)

3.  First thing you'll notice is that we want to be able to use three hyperparamters passed in, but the code is only expecting 1. You're task is to read in the other 2 hyperparameters into the script:

    ![](images/lab1/pic7.png)

4.  After making that change, you'll notice if you re-run the script in the jupyter notebook, then you'll see a different error:

    ![](images/lab1/pic8.png)

5.  Let's now check and update where it needs those parameter set in the file:

    ![](images/lab1/pic9.png)

6.  After setting the variables correctly being passed to the classifier, you should see this:

    ![](images/lab1/pic10.png)

7.  Let's test reading in the model and inferring here before jumping to the SageMaker training  

    This next cell re-reads in the classifier and infers on teh training data (usually this would be a different dataset)

    ![](images/lab1/pic11.png)


Step 4
------

Scikit Learn Estimator training through SageMaker

1.  Next we'll launch into a different notebook that uses the SageMaker Scikit learn Estimator to train our model.  

    Launch the 02\_TrainingInSageMaker.ipynb notebook

    ![](images/lab1/pic12.png)

2.  Run the first cell, this will setup the IAM role that the SageMaker uses to do the training  

    **NOTE:** it's important to keep this least priv in production

    ![](images/lab1/pic13.png)

3.  This next cell uploads the training data for the training job.  
    we see the location that the training containers will be passed printed at the end of the execution of this cell.

    ![](images/lab1/pic14.png)

4.  Next we'll create the Scikit Estimator. Notice we pass:  
    Script Location  
    Role/session info  
    Hyperparamters  
    Additional training instance size information

    ![](images/lab1/pic15.png)

5.  Running the next call actually triggers the training job via the "fit" call.  

    The parameters are passing in the "train" channel with the S3 location that we created and loaded the dataset to earlier.

    ![](images/lab1/pic16a.png)

    As it's training, you'll also notice the training job executing if you go to the SageMaker console under Training Jobs:

    ![](images/lab1/pic16b.png)

    You'll also notice the script gets executed the same way passing in the hyperparameters as the notebook we were testing with before:

    ![](images/lab1/pic16c.png)


Step 5
------

Testing the Model Locally

1.  Since we just built a model, we can see where the job stored it as well as the training job name:

    ![](images/lab1/pic17.png)

2.  Next, we'll download the model locally, and unpack it, load the classifier

    ![](images/lab1/pic18.png)

3.  Test some inferencing....

    ![](images/lab1/pic19.png)


© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
