# Doberman WebApp #

**Author: L. Bütikofer**

Date: 18. July 2016


## Brief ##

*Doberman WebApp* is an application based on Django in order to display, monitor and extract recorded data from the [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman) software. It is not a prerequisite to run the *Doberman slow control*, but allows for online visually inspection of the monitored system or analyze/extract data at a later time. 


## Prerequisites ##

The code is based on python 3 on linux. *Doberman WebApp* does not have to be running on the same machine as [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman). However [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman) has to be installed somewhere and should be accessible from the machine you are going to install *Doberman WebApp*.

## Installation ##
Installation guide tested for linux ubuntu 16.04 LTS

This installation guide assumes that you already fully completed the installation guide for [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman).


* Install pip3: `sudo apt install python3-pip`.
* Install Django web framework: `pip3 install django`.
* Install django-dbarray0.2:
    * `sudo apt-get install postgresql`
    * `sudo apt-get install python3-psycopg2`
    * `sudo apt-get install libpq-dev`
    * Download django-dbarray0.2 from [here](https://pypi.python.org/pypi/django-dbarray/0.2).
    * Extract file: `tar -xzvf django-dbarray-0.2.tar.gz`.
    * Install django-dbarray: `sudo python3 setup.py install`.
* Download *Doberman WebApp* to a directory of your choice: `git clone https://Doberman_slowcontrol@bitbucket.org/Doberman_slowcontrol/webapp.git`

* In your Web-app folder open the file *slow/settings.py* and go to the section below and change the settings according to the database you would like to connect to (i.e. the database you set up during the installation of [Doberman slow control](https://bitbucket.org/Doberman_slowcontrol/doberman)): 
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
* You should also add your host to the setting file option **ALLOWED_HOSTS = ['yourhost.com']**. (if you run the app only locally this could be 'localhost', see also the [documentation here](https://docs.djangoproject.com/en/1.9/ref/settings/#allowed-hosts)).
* After you modified the setup.py file run `python3 manage.py migrate`

### Set up the WebApp with apache ###
* `sudo apt-get install apache2`
* `sudo apt-get install apache2-dev`
* `sudo apt-get install libapache2-mod-wsgi-py3`
*  Add the following lines to the apache2.conf file (located in /etc/apache2):
    * replace */paht/to/your/app* with the directory where you installed *Doberman WebApp*, but leave the rest of the path as it already is in the file.
```
#!python
WSGIScriptAlias / /paht/to/your/app/slow/wsgi.py
WSGIPythonPath /paht/to/your/app
 
Alias /static/ /paht/to/your/app/static/
 
<Directory /paht/to/your/app/static>
Require all granted
</Directory>
 
<Directory /paht/to/your/app/slow>
	<Files wsgi.py>
		Require all granted
	</Files>
</Directory>
```
* Inside the file **/directory to WebApp/slow/wsgi.py** replace the line */directory/path/to/your/WebApp/location* with the directory you installed *Doberman WebApp* (don't replace */slow*)
* Enable “wsgi mod” by typing: `sudo a2enmod wsgi`
* Restart the server `sudo service apache2 restart`.
* Now you should be able to reach the Web-app at http://localhost/display (or http://your_IP_address/display).

## Optional: set up password log in ##
There are ways to add simple single user/password protection to your *Doberman WebApp*. See for example these instructions here https://github.com/plumdog/django-password-protect