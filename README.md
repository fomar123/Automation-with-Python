# To see what vpcs you have in AWS using boto3
<img width="662" alt="Screenshot 2023-07-05 at 23 06 00" src="https://github.com/fomar123/Automation-with-Python/assets/90075757/4eaa7d6b-e177-44b4-a806-788d9c67901c">


# Create VPCS and Subnets using Python:
<img width="735" alt="Screenshot 2023-07-05 at 22 59 49" src="https://github.com/fomar123/Automation-with-Python/assets/90075757/fcb831dd-e9f0-477a-84bf-df3b42c32797">

# Project: EC2 Server Status Checks Preparation

##### In this project, the goal is to prepare EC2 server status checks by creating instances with Terraform and then monitoring their states. 

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

##### This project involves implementing a data backup solution for EC2 instances through a Python script. 

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

# Project: EC2 Snapshots Cleanup using Python Script

##### This project aims to automate the cleanup of EC2 snapshots using a Python script. 

##### Step 1: Preparation - Create EC2 Instances with Environment Tags:
- Launch two EC2 instances and assign environment tags to differentiate between them.

##### Step 2: Get All EC2 Snapshots:
- Retrieve a list of all EC2 snapshots associated with the instances. This is crucial for snapshot management.

##### Step 3: Delete Excess Snapshots - Keep the Latest 2:
- Develop a Python script that identifies and deletes snapshots, retaining only the latest 2 snapshots for each volume.

##### Step 4: Write Scheduled Task for Cleanup:
- Schedule the Python script to run periodically (using a scheduler like cron) to automate the snapshot cleanup process.



##### Step 5: Check Your Progress:
- Validate that you've completed 3 out of the 5 steps outlined in the project.



# Project: Website Monitoring with Python Script

##### The goal of this project is to monitor a website and automate actions in response to various scenarios. 
##### Step 1: Preparation: Setting Up the Environment
- Create a server on Linode to host the website.
- Install Docker on the server.
- Run an nginx container to serve the website content.
- Validate requests to the nginx website to ensure it's functioning as expected.
  
##### Step 2: Python Script for Website Monitoring and Email Alerts
- Develop a Python script to monitor the website's availability and send email alerts for specific conditions.
- Handle scenarios where the website is down (HTTP status other than 200 - OK) or connection errors occur.
- Configure the script to use your email provider (e.g., Gmail) for sending emails.
- Set up environment variables to securely store email credentials.
  
##### Step 3: Python Script for Server Management
- Create a Python script to establish an SSH connection to the server.
- Automate the process of restarting the Docker container.
- Implement a server reboot procedure.
  
##### Step 4: Connect to Linode and Reboot Server
- Create an access token in Linode to interact with their.
- Utilise the Linode API module to connect to your Linode account.
- Perform a server reboot and restart the Docker container using the.
  
##### Step 5: Schedule the Website Monitoring and Server Management
- Implement a scheduled task to run the website monitoring script at regular intervals.
- Ensure the script executes the required actions, such as sending alerts and managing the server.
