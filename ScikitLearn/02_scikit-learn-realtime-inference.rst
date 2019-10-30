
Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     


.. image:: images/aws_logo.png
   :target: images/aws_logo.png
   :alt: 


Realtime Inferencing from the SciKit HPO Job
============================================

Step 1
------

Introduction

In this section, we'll take the best training job from HPO and deploy a realtime endpoint.

Step 2
------

Deploying our endpoint


#. Select the 004_RealtimeInferencinginSageMaker.ipynb notebook
#. 
   **IMPORTANT: fill in the HPO Job name. The screenshot shows an example filled in. you want to replace the ENTER_HPO_JOBNAME_HERE with your HPO job name


   .. image:: images/lab3/pic1.png
      :target: images/lab3/pic1.png
      :alt: 


   **
   ***   Next we'll deploy the endpoint from the HPO Tuning Job object


   .. image:: images/lab3/pic2.png
      :target: images/lab3/pic2.png
      :alt: 


   **This can take a few minutes to deploy**


* Next cell reads in some sample data to predict on
* 
  Next we'll compare our predictions against the actual values:


  .. image:: images/lab3/pic3.png
     :target: images/lab3/pic3.png
     :alt: 


* 
  Let's delete our realtime endpoint


  .. image:: images/lab3/pic4.png
     :target: images/lab3/pic4.png
     :alt: 

  **

**

© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.

**
