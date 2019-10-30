.. role:: raw-html-m2r(raw)
   :format: html


  Amazon SageMaker Workshop 

Anomaly Detection with Random Cut Forest
========================================

Step 1
------

Setting Up S3

This lab demonstrates how you can use the Random Cut Forest Amazon provided algorithm.

**IMPORTANT:**\ :raw-html-m2r:`<br>`
Replace the S3Bucket location with a bucket you created in the Lab1 of the workshop  


.. image:: images/lab1/pic1.png
   :target: images/lab1/pic1.png
   :alt: 


AFTER replacing the bucket location Run the first two cells\ :raw-html-m2r:`<br>`
You should see a message indicating where the S3 location being used is:


.. image:: images/lab1/pic2.png
   :target: images/lab1/pic2.png
   :alt: 


Step 2
------

Act 1 - Data download and exploration

Run through the data exploration cells in Act 1:\ :raw-html-m2r:`<br>`
Let's begin exploring the data.

Look at the data, can you start seeing any anomalies as we bin the data in diferent catagories\ :raw-html-m2r:`<br>`
Can you start to see any in the plots or table views?


.. image:: images/lab1/pic3.png
   :target: images/lab1/pic3.png
   :alt: 


One spike stands out...but there are likely more than that in this dataset...

Step 3
------

Act 2 - Training the Random Cut Forest

Go ahead and tep through Act 2 - training the model Take a look at the instance type and count. Notice that we can use different types and instances This process takes approximately 5 minutes to train. it's normal to see this type of output:


.. image:: images/lab1/pic4.png
   :target: images/lab1/pic4.png
   :alt: 


When it's done, you can execute the next cell and see the details here:


.. image:: images/lab1/pic5.png
   :target: images/lab1/pic5.png
   :alt: 


Step 4
------

Act 3 - Inferencing and Evluatingt

Create the endpoint to and run through the act 3 cells. Take a look at the anomaly score for some of the datapoints:


.. image:: images/lab1/pic6.png
   :target: images/lab1/pic6.png
   :alt: 


We can also examine the visual of the chart for the score over time:


.. image:: images/lab1/pic7.png
   :target: images/lab1/pic7.png
   :alt: 


Lets now look at more of the dataset:


.. image:: images/lab1/pic8.png
   :target: images/lab1/pic8.png
   :alt: 


Lastly, let's plot the points differently:


.. image:: images/lab1/pic9.png
   :target: images/lab1/pic9.png
   :alt: 


Step 5
------

Act 4 - Shingling to improve the model

Another improvement is make use of a windowing technique called "shingling".¶ This is especially useful when working with periodic data with known period, such as the NYC taxi dataset used above. The idea is to treat a period of PP datapoints as a single datapoint of feature length PP and then run the RCF algorithm on these feature vectors. That is, if our original data consists of points x1,x2,…,xN∈ℝx1,x2,…,xN∈R then we perform the transformation, Let's shingle the data per day.


.. image:: images/lab1/pic10.png
   :target: images/lab1/pic10.png
   :alt: 


Run the new training job


.. image:: images/lab1/pic11.png
   :target: images/lab1/pic11.png
   :alt: 


Step through the rest of the cells -- but take special attention to the results now:


.. image:: images/lab1/pic12.png
   :target: images/lab1/pic12.png
   :alt: 


© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
