# Teaching Tool for Demonstrating Digital Security Weaknesses
## Background
As we move to an ever increasing mobile technology orientated environment digital security is increasingly important. Loss of or compromised client/company data can have devastating consequences, both financial and reputational. As a result software engineers have an increasing responsibility to understand security issues in the applications they develop.

## Authors
The University of Glasgow's Third Year 2013/14 Team P comprises of the following individuals:

* Arnas Binkauskas
* Donald Martin
* Joshua McGhee
* Irina Preda

## Installation
### Requirements
Django

### Build Instructions
To obtain the source for the project, execute the following line in a terminal:
	git clone https://username@bitbucket.org/guteamp/web-app.git

If you are unable to access HTTPS from your system, an SSH clone can be done as follows:
	git clone git@bitbucket.org:guteamp/web-app.git

For information on how to setup an SSH key, visit Bitbucket's website.

### Running the Server
Execute the following line in a terminal:
    python manage.py runserver

## Administrivia
### Default User Login
* Username is "test"
* Password is "password"

### Default Administrator Login
* Username is "test"
* Password is "password"

### Pure Lesson Pages
As the source code for each of the lessons is stored an an SQLite database, I have created a directory in which to store this source code independently, should it need reviewed away from a running system.
