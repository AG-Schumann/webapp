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


1. Install pip3: `sudo apt install python3-pip`.
2. Install Django web framework: `sudo pip3 install django`.
3. Install django-dbarray0.2:
    * Download django-dbarray0.2 from [here](https://pypi.python.org/pypi/django-dbarray/0.2).
    * Extract file: `tar -xzvf file.tar.gz`.
    * Install django-dbarray: `sudo python3 setup.py install`.
4. Download *Doberman WebApp* to a directory: `git clone https://Doberman_slowcontrol@bitbucket.org/Doberman_slowcontrol/webapp.git`




1. Create a virtual environment (Steps shown for Anaconda):
     * Download and install Anaconda for python 2.7 for linux by following the steps (step 1 and 3, step 2 is optional) on https://www.continuum.io/downloads (at "Linux Anaconda Installation") and accept everything required.
     * Open a new terminal to activate the Anaconda installation. If you did not include conda to your bash path, make sure to add it before each command or navigate to the anaconda directory.
     * Create an virtual environment, e.g. called 'Doberman', (incl. postgresql and pip packages) with `conda create --name Doberman postgresql pip` and accept the package downloads. (Be aware that OpenSSH is delivered with this packages for remote control and make sure your computer is protected sufficiently).
     * Activate environment with `source activate Doberman`.
2.  Download this repository to a directory (e.g. `git clone https://Doberman_slowcontrol@bitbucket.org/Doberman_slowcontrol/doberman.git`).
3.  Install and create a PostgreSLQ Database (These steps are for a local database, it is also possible to separate Doberman and the database. Tutorials: https://help.ubuntu.com/community/PostgreSQL). Steps (for a local server):
     * Download posgresql: `sudo apt-get install postgresql postgresql-contrib`.
     * Create the role 'postgres' with `sudo -u postgres psql postgres` and choose a password with `\password postgres`.
     * Optionally (recommended): Create additional roles with different access rights. (https://www.postgresql.org/docs/8.1/static/sql-createrole.html)
     * Quit postgres with `\q`
     * Create a database, e.g. named "Doberman", with `sudo -u postgres createdb Doberman`.
4. Write the connection details according to the database name (e.g. Doberman), password and role ("postgres" or name of the additionally created role) used in step 3. to the txt file '*Database_connectiondetails.txt*' located in the Doberman folder. (Maintain the format, use host='localhost' if database is not separated from Doberman)
5. Install python and required packages by running `pip install -r [PATH/TO/Doberman/]requirements.txt`. (Check the wiki if errors occur)
6. Fill out the files '*MAIL_connectiondetails.txt*' and '*SMS_connectiondetails.txt*' for the warning and alarm distribution.
7. To create the tables in the database run `python Doberman.py -n` in the terminal. Confirm that you want to create all the tables (Don't start Doberman yet).
8. Add your Plugins. Make sure you follow the steps on wiki (https://bitbucket.org/Doberman_slowcontrol/doberman/wiki/Home -> "Add a new Plugin") on how to add and properly write the Plugin specific code and where to save it.
9. Optionally: Manage your settings (contacts, defaults, etc.) as described below ("Manage Settings").
10. Optionally: Install the Web-App if required. ** MISSING: Link to Web-App **
## Usage ##

### Run main program ###
Navigate to your Doberman slow control folder and run `python Doberman.py [-opts]` script.

The different options '*-opt*' are:

* -t[=x]: Test modus: No alarms will be sent [for the first x minutes] (default t=2 minutes).

* -d=x: (debug) Log level: What messages get to the terminal/the log files (x=10: debug, x=20: info, x=30: warning (default), x=40: error, x=50: critical)

* -i=x: Import timeout: Timeout for each plugin at the import (x in seconds). (Default i=10 s)

* -o=x[,y,]: Occupied ttyUSB ports: Use this option if the Doberman slow control should not connect to a [several] ttyUSB port x [and y,...]. This can be useful if you don't want to disturb a controller which is already connected.

* -wr: Warning repetition: Minimal time after a warning or alarm until a new warning can be sent for each plugin and each channel (Default wr=10 min).

* -ar: Alarm repetition: Minimal time after an alarm before a new alarm can be sent for each plugin and each channel (Default ar=5 min).

* -f[filename]: Filereading: Read your plugins settings from the file [filename] or default file (default=configBackup.txt)

## Manage Settings ##
### Add/remove a plugin to/from the settings ###
* Run `python Doberman.py -a` in the terminal to add a plugin or `python Doberman.py -r` to remove one.
* Make sure you follow the steps on wiki (https://bitbucket.org/Doberman_slowcontrol/doberman/wiki/Home -> Add a new Plugin) on how to properly write the controller specific code and where to save it.
* Optionally a plugin can be added in a file (same structure as backup file 'configBackup.txt' needed) and Doberman has to be run with -f=filename. (Warning: The format and values are not controlled when using this method).
### Change/update plugin settings ###
* Run `python Doberman.py -u` in the terminal to update status, alarm status and all alarm/warning limits
* or `python Doberman.py -uu` to update all config parameters.
* Optionally the changes can be made in a file (same structure as backup file 'configBackup.txt' needed) and Doberman has to be run with -f=filename. (Warning: The format and values are not controlled when using this method).
### Manage contatacts for alarm/warning distribution ###
Run `python Doberman.py -c` in the terminal to add, change, enable/disable and remove contacts from the list.
### Update default values ###
Run `python Doberman.py -ud` in the terminal to update the default values for testrun time (-t), loglevel (-d), importtimeout (-i), occupied ttyUSB ports (-o), warning repetition time (-wr) and alarm repetition time (-ar)