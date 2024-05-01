<h1 align="center"> Email Notification for CPU/RAM spike using Python script </h1>


<br>
<br>

<h1 align="center">Lets Begin </h1>


## Process
-  Created a terraform code to deploy EC2 spot instance in AWS.
-  Install python and needed library for the Python script.
    - `apt install python3 python3-pip`
    - `pip install psutil`
-  Developed the Python script to send Email when the cpu or the ram breach the specified metric.
-  Run the script. 
