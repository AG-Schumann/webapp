# Doberman WebApp #

**Author: L. Bütikofer**

Date: 18. July 2016


## Brief ##

*Doberman WebApp* is an application based on Django in order to display, monitor and extract recorded data from the [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman) software. It is not a prerequisite to run the *Doberman slow control*, but allows for online visually inspection of the monitored system or analyze/extract data at a later time. 


## Prerequisites ##

The code is based on python 3 on linux. *Doberman WebApp* does not have to be running on the same machine as [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman). However [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman) has to be installed somewhere and should be accessible from the machine you are going to install *Doberman WebApp*.

PostgreSQL

psycopg2 (for django db array ?)

## Installation ##
Installation guide tested for linux ubuntu 16.04 LTS

This installation guide assumes that you already fully completed the installation guide for [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman).


* Install pip3: `sudo apt install python3-pip`.
* Install Django web framework: `sudo pip3 install django`.
* Install django-dbarray0.2:
    * `sudo apt-get install postgresql`
    * `sudo apt-get install python3-psycopg2`
    * `sudo apt-get install libpq-dev`
    * Download django-dbarray0.2 from [here](https://pypi.python.org/pypi/django-dbarray/0.2).
    * Extract file: `tar -xzvf file.tar.gz`.
    * Install django-dbarray: `sudo python3 setup.py install`.
* Download *Doberman WebApp* to a directory: `git clone https://Doberman_slowcontrol@bitbucket.org/Doberman_slowcontrol/webapp.git`

* In your Web-app folder open the file *slow/settings.py* and go to the section below andchange the settings according to the database you would like to connect to (i.e. the database you set up during the installation of [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman)): 
```
#!python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_DB_name',
        'USER': 'your_DB_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_DB_host',
        'PORT': 'your_DB_port',
    }
}
```
* `python3 manage.py migrate`
* `sudo apt-get install aptitude`
* `sudo aptitude install apache2 apache2.2-common apache2-mpm-prefork apache2-utils libexpat1 ssl-cert`
* `sudo pip3 install mod_wsgi`
