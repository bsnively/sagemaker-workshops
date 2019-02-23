Amazon SageMaker Workshop                              if ( $.cookie('styleCookie') === 'style-light.css') { $('html, body').css('background', '#eeeeee'); } else if ($.cookie('styleCookie') === 'style.css') { $('html, body').css('background', '#222222'); }                     

![](images/aws_logo.png)

Lab 5:  
Batch Inferencing from the SciKit HPO Job
====================================================

Step 1
------

Introduction

In this section, we'll take the best training job from HPO and perform batch inferencing using the model

Step 2
------

Deploying our endpoint

1.  Select the 05\_BatchInferencinginSageMaker.ipynb notebook
2.  **IMPORTANT: fill in the HPO Job name. The screenshot shows an example filled in. you want to replace the ENTER\_HPO\_JOBNAME\_HERE with your HPO job name

  ![](images/lab4/pic1.png)

  **
***   From the HPO configuration, we can attach the SKLearn estimator using the sagemaker session and job name.

  ![](images/lab4/pic2.png)

  **This can take a few minutes to deploy**
*   Next we create our transformer

  ![](images/lab4/pic3.png)

*   In the next 3 cells, we'll create some sample data, upload them to S3, and start our batch transformation job:

  ![](images/lab4/pic4.png)

  You can also go in sagemaker console and look under batch transform jobs to see the job there

  ![](images/lab4/pic4b.png)

*   When the job finishes, look in the console at the details of the job and click the link to see the output results:

  ![](images/lab4/pic5a.png)

  This will bring you into S3 where the results are:

  ![](images/lab4/pic5b.png)

*   Let's continue in the notebook  
  Run the next two cells to see the batch results

  ![](images/lab4/pic6.png)
  **

**

© 2018, Amazon Web Services, Inc. or its affiliates. All rights reserved.
