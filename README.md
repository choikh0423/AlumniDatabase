# Alumni Database 
**Last updated: 4/25/2020**

This website is an **alumni database web application** intended to provide quick and easy search engine for organization members to find their alumni.

## Project Setup
### Installation
You will need python 3.7.2 and django 3.0.3 set up in your environment to run this project.

1. Install Python3 and Django
2. Clone this repository

### Running & Managing the Server
Make sure that you are in the right folder w/ manage.py:\
 `cd alumnidatabase` `ls`
 
To start running the server:\
`python3 manage.py runserver`

To experiment in a python shell environment:\
 `python3 manage.py shell`

## Personalization
1. Modify Email_Host, Email_Host_User, and Email_Host_Password in `settings.py` under `alumnidatabase` \
2. Modify superuser email and password - The current email and password for the superuser is username: admin, email:\  admin@alumnidatabase.com, pw: testadmin123 \
2-1. Log in through admin page with the email and pw and access Users -> admin -> modify email to your email. \ 
2-2. Change your password with `python3 manage.py changepassword`. Input username admin and the padssword that you want to change to. \

## Contributors
- Dongho Kim - Back-End Developer
- Jeeyoon Kim - UI/UX Designer
- Kyu Hwan Choi - Back-End & Front-End Developer
