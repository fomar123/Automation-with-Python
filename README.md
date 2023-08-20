# To see what vpcs you have in AWS using boto3
<img width="662" alt="Screenshot 2023-07-05 at 23 06 00" src="https://github.com/fomar123/Automation-with-Python/assets/90075757/4eaa7d6b-e177-44b4-a806-788d9c67901c">


# Create VPCS and Subnets using Python:
<img width="735" alt="Screenshot 2023-07-05 at 22 59 49" src="https://github.com/fomar123/Automation-with-Python/assets/90075757/fcb831dd-e9f0-477a-84bf-df3b42c32797">

# Project: EC2 Server Status Checks Preparation

##### In this project, the goal is to prepare EC2 server status checks by creating instances with Terraform and then monitoring their states. The following tasks are performed:

##### Creating EC2 Instances with Terraform:
- Using Terraform, three EC2 instances are created.

             terraform apply --auto-approve
  
##### Printing EC2 Instance States:
- Retrieving and printing the state (running, stopped, etc.) of all EC2 instances created.
  
##### Printing Status Checks of EC2 Instances:
- Displaying the status checks (system, instance) of all EC2 instances for health monitoring.

# Project: Scheduling the Status Checks
###### Install schedule library:
          Pip install schedule
###### Schedule status check every five seconds 
###### Schedule status check every five seconds

