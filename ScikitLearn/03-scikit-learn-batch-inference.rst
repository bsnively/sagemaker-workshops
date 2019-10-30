.. role:: raw-html-m2r(raw)
   :format: html


Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     


.. image:: images/aws_logo.png
   :target: images/aws_logo.png
   :alt: 


Lab 5:  

Batch Inferencing from the SciKit HPO Job
=========================================

Step 1
------

Introduction

In this section, we'll take the best training job from HPO and perform batch inferencing using the model

Step 2
------

Deploying our endpoint


#. Select the 05_BatchInferencinginSageMaker.ipynb notebook
#. 
   **IMPORTANT: fill in the HPO Job name. The screenshot shows an example filled in. you want to replace the ENTER_HPO_JOBNAME_HERE with your HPO job name


   .. image:: images/lab4/pic1.png
      :target: images/lab4/pic1.png
      :alt: 


   **
   ***   From the HPO configuration, we can attach the SKLearn estimator using the sagemaker session and job name.


   .. image:: images/lab4/pic2.png
      :target: images/lab4/pic2.png
      :alt: 


   **This can take a few minutes to deploy**


* 
  Next we create our transformer


  .. image:: images/lab4/pic3.png
     :target: images/lab4/pic3.png
     :alt: 


* 
  In the next 3 cells, we'll create some sample data, upload them to S3, and start our batch transformation job:


  .. image:: images/lab4/pic4.png
     :target: images/lab4/pic4.png
     :alt: 


  You can also go in sagemaker console and look under batch transform jobs to see the job there


  .. image:: images/lab4/pic4b.png
     :target: images/lab4/pic4b.png
     :alt: 


* 
  When the job finishes, look in the console at the details of the job and click the link to see the output results:


  .. image:: images/lab4/pic5a.png
     :target: images/lab4/pic5a.png
     :alt: 


  This will bring you into S3 where the results are:


  .. image:: images/lab4/pic5b.png
     :target: images/lab4/pic5b.png
     :alt: 


* 
  Let's continue in the notebook\ :raw-html-m2r:`<br>`
  Run the next two cells to see the batch results


  .. image:: images/lab4/pic6.png
     :target: images/lab4/pic6.png
     :alt: 

  **

**

© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
