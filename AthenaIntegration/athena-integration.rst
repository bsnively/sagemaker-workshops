.. role:: raw-html-m2r(raw)
   :format: html


  Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     


.. image:: images/aws_logo.png
   :target: images/aws_logo.png
   :alt: 


  Lab 4:  

Integrating with AWS Services (Athena)
======================================

Step 1
------

Introduction

In this section, we'll show how to start integrating with various Services.

Step 2
------

Integrating with Athena


#. 
   Select the IntegratingWithServices/AthenaExample.ipynb notebook


   .. image:: images/lab3/pic1.png
      :target: images/lab3/pic1.png
      :alt: 


#. 
   this will laumnch the notebook that has the athena exmaple. In this notebook we'll create the table in the Glue catalog. Ideally this would have be done through Glue, Lake Formation or another method. We wanted this to be a self contained notebook though.


   .. image:: images/lab3/pic2.png
      :target: images/lab3/pic2.png
      :alt: 


#. 
   This first cell will load pyathena\ :raw-html-m2r:`<br>`
   `https://pypi.org/project/PyAthena/ <https://pypi.org/project/PyAthena/>`_


   .. image:: images/lab3/pic3.png
      :target: images/lab3/pic3.png
      :alt: 


#. 
   Athena needs a S3 bucket location and a region setting when making the connection.\ :raw-html-m2r:`<br>`
   Rather than hard coding these, we are going to pull them from the sagemaker session.


   .. image:: images/lab3/pic4.png
      :target: images/lab3/pic4.png
      :alt: 


#. 
   Next we'll create a connection object


   .. image:: images/lab3/pic5.png
      :target: images/lab3/pic5.png
      :alt: 


#. 
   We'll create a flights table


   .. image:: images/lab3/pic6.png
      :target: images/lab3/pic6.png
      :alt: 


#. 
   This command is necessary because we did the create table ourselves and it's partitioned in S3. This discovers the partitions in the catalog


   .. image:: images/lab3/pic7.png
      :target: images/lab3/pic7.png
      :alt: 


#. 
   We can directly load our pandas dataframe now from Athena:


   .. image:: images/lab3/pic8.png
      :target: images/lab3/pic8.png
      :alt: 


#. 
   Let's create a seaborn heatmap based on delays per departing and arriving airport:


   .. image:: images/lab3/pic9.png
      :target: images/lab3/pic9.png
      :alt: 


© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
