# Lab 04 – AWS EC2 Automation and Web Server Deployment

**Overview**
This lab is part of the Master’s Degree in Cloud Computing at NCI and focuses on provisioning, configuring, and automating AWS EC2 instances using AWS CLI and Python (boto3).

---

**Objectives**

* Launch EC2 instances using AWS CLI
* Configure AWS authentication credentials securely
* Install and validate a web server on EC2
* Automate instance lifecycle using Python
* Query AWS resources dynamically
* Terminate instances programmatically

---

**Architecture Overview**
An AWS EC2 instance running Amazon Linux 2023 was used as a control node to execute AWS CLI commands and Python automation scripts. Additional EC2 instances were launched dynamically, configured automatically, validated through browser access, and terminated programmatically.

---

**Technologies and Tools**

* AWS EC2
* AWS CLI
* Python 3
* Boto3
* Amazon Linux 2023
* Nginx
* SSH

---

**Description**
The lab began with configuring AWS CLI credentials and setting the default region. Using command-line tools, EC2 instances were launched and verified. A Python script using boto3 was then executed to automate the creation and termination of instances.

A web server (Nginx) was installed to validate connectivity and server functionality. The successful execution confirmed that instances could be provisioned, configured, tested, and removed automatically using infrastructure automation techniques.

---

**Outputs**

* AWS CLI credentials configuration
  ![Credentials](./screenshots/01-configure-aws-cli-credentials.jpg)

* Region configuration
  ![Region](./screenshots/02-set-aws-region.jpg)

* Environment variables exported
  ![Env](./screenshots/03-aws-credentials-export.jpg)

* Python version verification
  ![Python](./screenshots/04-check-python-version.jpg)

* pip installation
  ![pip](./screenshots/05-install-python-pip.jpg)

* boto3 installation
  ![boto3](./screenshots/06-install-boto3.jpg)

* Key pair list via CLI
  ![Keys](./screenshots/07-list-keypairs-cli.jpg)

* Security groups list
  ![Security Groups](./screenshots/08-list-security-groups.jpg)

* EC2 instance launched via CLI
  ![Launch](./screenshots/09-run-instance-cli.jpg)

* Instance launched and terminated automatically
  ![Automation](./screenshots/10-launch-and-terminate-instance.jpg)

* Nginx installation
  ![Nginx](./screenshots/11-install-nginx.jpg)

* Nginx running in browser
  ![Browser](./screenshots/12-nginx-running-browser.jpg)

* Custom HTML test page
  ![HTML](./screenshots/13-browser-lab-page.jpg)

* Second instance running
  ![Instance](./screenshots/14-browser-new-instance.jpg)

* EC2 console instance list
  ![Console](./screenshots/15-ec2-console-instance-list.jpg)

* Latest Amazon AMIs list via CLI
  ![AMIs](./screenshots/16-list-amazon-amis-cli.jpg)

---

**Learning Outcomes**

* Understanding how to launch and manage EC2 instances via CLI
* Automating infrastructure using Python scripts
* Configuring cloud authentication securely
* Installing and validating web services on cloud VMs
* Querying AWS resources programmatically
* Managing instance lifecycle dynamically

---

**Conclusion**
This lab demonstrated how cloud infrastructure can be provisioned, configured, validated, and terminated automatically using scripting and command-line tools. The exercise highlights essential real-world cloud engineering skills such as automation, infrastructure lifecycle management, and programmatic control of cloud resources.
