# Gauss-The-Facts
## what we do

Gauss-The-Facts is a project designed to provide trivia questions that broaden knowledge with unexpected and intriguing answers. 
Users can also suggest interesting facts, which, upon approval, will be added to the trivia questions. 
This application aims to integrate continuous integration (CI) and continuous deployment (CD) using GitHub Actions,
deploying to AWS with infrastructure managed by Terraform.

## Prerequisites

Before you begin, ensure you have met the following requirements:

You have installed required software/tools, Python, Docker, mysql.
You have a relevant platform/OS - Ubuntu.

## Installation

Clone the repository:

```bash
$ git clone https://github.com/itay-elb/Gauss-The-Facts.git
$ cd Gauss-The-Facts
```

Install dependencies:

```bash
$ pip install -r requirements.txt
```

Set up the database:
Provide database setup instructions, e.g., docker-compose file
make sure you set up the connection beteen the database to the app 

Run the application:

```bash
$ docker-compose up
```

Now you have this applicaison local, you can challenge your friends with facts or add more facts of your own 

## level up

If you have an AWS user, you can make it an automatic process for creating the site and allow everyone to use it,
just make sure you replace the secrets with the secrets of your AWS user in the git actio n.
