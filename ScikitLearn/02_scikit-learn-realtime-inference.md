Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     

![](images/aws_logo.png)

Realtime Inferencing from the SciKit HPO Job
=======================================================

Step 1
------

Introduction

In this section, we'll take the best training job from HPO and deploy a realtime endpoint.

Step 2
------

Deploying our endpoint

1.  Select the 004\_RealtimeInferencinginSageMaker.ipynb notebook
2.  **IMPORTANT: fill in the HPO Job name. The screenshot shows an example filled in. you want to replace the ENTER\_HPO\_JOBNAME\_HERE with your HPO job name

  ![](images/lab3/pic1.png)

  **
***   Next we'll deploy the endpoint from the HPO Tuning Job object

  ![](images/lab3/pic2.png)

  **This can take a few minutes to deploy**
*   Next cell reads in some sample data to predict on
*   Next we'll compare our predictions against the actual values:

  ![](images/lab3/pic3.png)

*   Let's delete our realtime endpoint

  ![](images/lab3/pic4.png)
  **

**

© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.









**
