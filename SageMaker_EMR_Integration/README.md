## SageMaker/EMR Integration CloudFormation Template:
This contains a AWS CloudFormation Template that creates the following artifacts:

* New VPC with a Single Public Subnet
* EMR Cluster running (Hadoop, Hive, Spark, Livy)
    * Configurations:
        * 24 Hour Livy Timeout
        * Spark Maximum Resource Allocation
* SageMaker
    * Lifecycle Configuration configuring SparkMagic to Cluster
    * Notebook Instance

The following Diagram shows what gets created:

![alt text](overview_diagram.png "Logo Title Text 1")

The following is what is used to create the config on the notebook through the lifecycle configuration:

```sh
set -e
cd /home/ec2-user/.sparkmagic
wget https://raw.githubusercontent.com/jupyter-incubator/sparkmagic/master/sparkmagic/example_config.json
sed s/localhost/`aws emr list-instances --cluster-id ${EMR_CLUSTER_ID} --instance-group-types MASTER --query Instances[0].PrivateIpAddress --output text`/g example_config.json > config.json
```
