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

# Project: Data Backup for EC2 Instances using Python Script

##### This project involves implementing a data backup solution for EC2 instances through a Python script. The project workflow includes the following steps:

##### Step 1: Preparation - Create EC2 Instances with Environment Tags:
- Create two EC2 instances and assign environment tags (e.g., production, development) to them for differentiation.

##### Step 2: Get Volume IDs:
- Retrieve the Volume IDs associated with the EC2 instances. This is essential for snapshot creation.

##### Step 3: Create Snapshots from Volume IDs:
- Use the Volume IDs to create snapshots of the associated volumes for data backup.

##### Step 4: Write Scheduled Task for Backup:
- Implement a scheduled task (e.g., cron job) that triggers the Python script to run periodically, ensuring automated backups.

##### Step 5: Create Snapshots only for Production Servers:
- Implement a condition in the Python script to create snapshots only for instances with the "production" environment tag.
