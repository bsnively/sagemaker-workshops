.. role:: raw-html-m2r(raw)
   :format: html


   Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     


.. image:: images/aws_logo.png
   :target: images/aws_logo.png
   :alt: 


  Lab 3:  

KMeans Clustering
=================

Step 1
------

Introduction

K-means is an unsupervised learning algorithm. It attempts to find discrete groupings within data, where members of a group are as similar as possible to one another and as different as possible from members of other groups. You define the attributes that you want the algorithm to use to determine similarity. Amazon SageMaker uses a modified version of the web-scale k-means clustering algorithm. Compared with the original version of the algorithm, the version used by Amazon SageMaker is more accurate. Like the original algorithm, it scales to massive datasets and delivers improvements in training time. To do this, the version used by Amazon SageMaker streams mini-batches (small, random subsets) of the training data. For more information about mini-batch k-means, see Web-scale k-means Clustering.

Step 2
------

Loading the Notebook


#. Download the base notebook: `KMeansOfCrimeData.ipynb <KMeansOfCrimeData.ipynb>`_
#. Open the notebook instance and upload the notebook
#. First set the S3 bucket that you created in Lab1


.. image:: images/lab2/pic0.png
   :target: images/lab2/pic0.png
   :alt: 



#. 
   Let's load the data and look at it:\ :raw-html-m2r:`<br>`
   Run the next cell to download the dataset to the notebook\ :raw-html-m2r:`<br>`
   Look at the two datasets we have here.\ :raw-html-m2r:`<br>`
   (1) The Crime data include state and crime stats\ :raw-html-m2r:`<br>`
   (2) The Density data include state and density numbers  


   .. image:: images/lab2/pic1.png
      :target: images/lab2/pic1.png
      :alt: 


#. 
   Since we have mixed numerical values that really are different units and scales\ :raw-html-m2r:`<br>`
   The scale on the density is much greater than the scale of our other features.\ :raw-html-m2r:`<br>`
   Let's scale it back to between -1 and 1:


   .. image:: images/lab2/pic2.png
      :target: images/lab2/pic2.png
      :alt: 


#. 
   Let's join this dataset together next so we can cluster on the combined fields


   .. image:: images/lab2/pic3.png
      :target: images/lab2/pic3.png
      :alt: 


#. 
   In the next section, we'll do the following\ :raw-html-m2r:`<br>`
   First we'll create an array of floats. These are the values used in the clustering algorithms\ :raw-html-m2r:`<br>`
   Next we'll check the dimension, or shape, of the values. Not surprising it's 50 since it's per state and we see 5 features\ :raw-html-m2r:`<br>`
   Last, we print the values to look at them...  


   .. image:: images/lab2/pic4.png
      :target: images/lab2/pic4.png
      :alt: 


Step 3
------

Training the KMeans Cluster


#. 
   Run the next cell to setup the kmean training information\ :raw-html-m2r:`<br>`
   Take special attention to the Hyperparamters...


   .. image:: images/lab2/pic7.png
      :target: images/lab2/pic7.png
      :alt: 


.. code-block::

   **Important:** Notice how we are using the **from sagemaker import KMeans** rather than a container in this example  
   This is using the SageMaker SDK libraries.


#. 
   Run the KMeans fit method to train the model


   .. image:: images/lab2/pic8.png
      :target: images/lab2/pic8.png
      :alt: 


   After a few minutes, you'll see the build process to start:


   .. image:: images/lab2/pic8b.png
      :target: images/lab2/pic8b.png
      :alt: 


#. 
   After the model is built, notice how the wall time and bill time is different.\ :raw-html-m2r:`<br>`
   You aren't charged startup costs for the cluster.


   .. image:: images/lab2/pic9.png
      :target: images/lab2/pic9.png
      :alt: 


Step 4
------

Deploying the model endpoint


#. 
   Deploy the model. This can take a few minutes...


   .. image:: images/lab2/pic10.png
      :target: images/lab2/pic10.png
      :alt: 


   In this example, the endpoint took 5 minutes to come up:


   .. image:: images/lab2/pic11.png
      :target: images/lab2/pic11.png
      :alt: 


#. 
   Let's run some predictions and look at the results


   .. image:: images/lab2/pic12.png
      :target: images/lab2/pic12.png
      :alt: 


#. 
   Sort by cluster group and the distance from the cluster center or cluster mean:


   .. image:: images/lab2/pic13.png
      :target: images/lab2/pic13.png
      :alt: 


#. 
   Lastly, we'll show the distribution of data across each cluster:


   .. image:: images/lab2/pic14.png
      :target: images/lab2/pic14.png
      :alt: 


   This shows us how large each cluster is (assuming we assign the data point to the closest cluster...)

© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
