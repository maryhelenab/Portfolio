# Cloud Platform Programming – NCI

This lab is part of the **Cloud Platform Programming** module of the **Master’s Degree in Cloud Computing** at the **National College of Ireland (NCI)**.

The objective of this lab is to deploy a **Django web application to the AWS cloud** using **AWS Elastic Beanstalk**. The lab demonstrates how a Python web application can be packaged, configured, and deployed to a cloud platform with minimal infrastructure management.

---

# Lab 05 – Deploying a Django Application with AWS Elastic Beanstalk

This lab focuses on deploying a Django application using **AWS Elastic Beanstalk**, a Platform-as-a-Service (PaaS) offering from Amazon Web Services.

Elastic Beanstalk automatically handles:

- provisioning EC2 instances
- configuring load balancing
- setting up scaling
- managing deployment environments

The application is uploaded to AWS, where Elastic Beanstalk automatically builds the environment and runs the application.

---

# Key Concepts

This lab introduces important cloud deployment concepts:

- Platform as a Service (PaaS)
- AWS Elastic Beanstalk
- Cloud deployment workflows
- Django application configuration for production
- Environment configuration using `.ebextensions`
- Cloud infrastructure automation

---

# Tasks Completed

The following tasks were performed during the lab:

- Creation of a **Django project**
- Setup of a **Python virtual environment**
- Installation of project dependencies
- Creation of a **requirements.txt** file
- Configuration of **Elastic Beanstalk CLI**
- Initialization of an Elastic Beanstalk application
- Creation of a deployment environment
- Configuration of deployment settings using `.ebextensions`
- Deployment of the Django application to AWS
- Verification of the running application in the cloud

---

# Elastic Beanstalk Configuration

Elastic Beanstalk configuration files were created inside the following directory:

```
.ebextensions/
```

These configuration files allow customization of the deployment environment, such as:

- environment settings
- package installation
- application configuration

---

# Project Structure

```
lab-05-elasticbeanstalk-python-django-lab/
│
├── screenshots/
│
├── simple_proj/
│   └── demoproj/
│       ├── .ebextensions/
│       ├── .elasticbeanstalk/
│       │
│       ├── demoproj/
│       │   ├── __init__.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       │
│       ├── env/
│       ├── .gitignore
│       ├── db.sqlite3
│       ├── manage.py
│       └── requirements.txt
│
└── README.md
```

---

# Deployment Steps

The following commands were used to deploy the application to AWS Elastic Beanstalk.

### Initialize Elastic Beanstalk

```bash
eb init -r us-east-1 -p python-3.8 simpledemo
```

### Create Environment

```bash
eb create myenv --service-role LabRole --instance_profile LabInstanceProfile
```

### Deploy Application

```bash
eb deploy
```

### Check Environment Status

```bash
eb status
```

### Open Application in Browser

```bash
eb open
```

---

# Running the Project Locally

Before deploying, the application can be tested locally.

```bash
cd simple_proj/demoproj
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The application will run at:

```
http://127.0.0.1:8000
```

---

# Learning Outcome

After completing this lab, the following skills were developed:

- Deploying Python applications to AWS
- Understanding Platform-as-a-Service cloud environments
- Configuring Django applications for cloud deployment
- Using the **Elastic Beanstalk CLI**
- Managing application environments in AWS
- Understanding automated infrastructure provisioning

These concepts are fundamental for building and deploying **cloud-native applications** using modern cloud platforms.
