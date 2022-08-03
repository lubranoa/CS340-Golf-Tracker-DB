# CS340-Golf-Tracker-DB

#### Created by Conner Marchell and Alex Lubrano for CS 340 - Introduction to Databases

## Overview

This README covers a brief description of our project and how to set it up using Oregon State's ENGR servers and our course's MySQL database. The setup guide is intended for a student, TA, or professor that has not initialized a repository or directory for this project. If you are not pulling the repository from GitHub and already have the files, take care to ensure the file structure remains the same as in the Directory Structure section below. The setup guide uses the CLI methods described in the explorations to set up the project.

## Table of Contents
- [Overview](#overview)
- [Project Description](#project-description)
- [Project Setup](#project-setup)
- [Directory Structure](#directory-structure)
- [Links](#links)

## Project Description
Description goes here.

## Project Setup
**1.** SSH into your flipX server of choice.

**2.** If you want to pull the files from GitHub, `cd` into the directory you want the repo in. Otherwise, if you already have the files, move them into the desired directory and skip to **Step 4**.

**3.** If you have github ssh set up like they showed us in this course and you want to clone using ssh, run the first line. Otherwise, if you want to use username/password, run the second line.

```bash
git clone git@github.com:lubranoa/CS340-Golf-Tracker-DB.git

# OR

git clone https://github.com/lubranoa/CS340-Golf-Tracker-DB.git
```

**4.** Confirm that the project files are located in the proper directories. The files and directories do not need to be in any particular order, just in the proper locations, as shown here:

```
.
├── .gitignore
├── README.md
├── app.py
├── wsgi.py
├── requirements.txt
├── venv
├── static
│    └ css                    <= Contains all project.css files
│        ├ all-templates.css
│        └ # etc.
├── database
│    ├ db_connector.py
│    ├ golf-tracker-DDQ.sql
│    └ golf-tracker-DMQ.sql
└── templates                 <= Contains all project.j2 files
     ├ main.j2
     └ # etc.
```

**5.** Next, `cd` into the root of the project directory (if not already in it) and set up a Python virtual environment by running these three lines separately in the command line:
```bash
cd project-dir/

pip3 install --user virtualenv

python3 -m venv ./venv
```

**6.** Activate the virtual environment (always do this when setting up or working on the project) by running:
```bash
source ./venv/bin/activate
```
   - If you want to confirm the virtual environment is active, run the following commad:
```bash
which python3
# should return <path_to_your_repo_folder>/venv/bin/python3
```
   - To leave the virtual environment, run `deactivate`

**7.** Install the dependencies in `requirements.txt` by running:
```bash
pip3 install -r requirements.txt
```

**8.** Create a .env file in the root project directory running `touch .env` and add the following lines to it, changing the bottom three values to your own credentials. Ensure that the .env file is in the .gitignore file for credential security.
```bash
340DBHOST = 'classmysql.engr.oregonstate.edu'
340DBUSER = '<your_osu_db_user_name>'  # cs340_onid
340DBPW = '<your_osu_db_password>'     # 4-digit pw to log in to db
340DB = '<your_osu_db_name>'           # cs340_onid
```

**9.** (Optional) `cd` into the project's `/database` directory and create a backup of your current database:
```bash
mysqldump -u cs340_onid -h classmysql.engr.oregonstate.edu -p cs340_onid > backup.sql
```

**10.** If not already in the project's `/database` directory, `cd` into it, then log in to your database by running:
```bash
mysql -u cs340_onid -h classmysql.engr.oregonstate.edu -p cs340_onid
```

**11.** (Optional) Drop any tables that you may want to from your osu database using: ```DROP TABLES your_table1, your_table2;```

**12.** Load ```golf-tracker-DDQ.sql``` into your database, entering:
```
source golf_tracker_DDQ.sql
```

**13.** Ensure there were no issues importing, then exit the OSU database by entering `exit;`

**14.** To run the web app, there are two options to choose from, running on localhost or persistently using gunicorn. If you want to run via gunicorn, skip to **Step 16**, otherwise continue to **Step 15**.

**15.** To run via localhost, `cd` into the root directory if not in it already. Run the following command. There is no need to change the port in `test_app.py` unless you are already using port 15434 for something else:
```bash
python3 test_app.py
```
You will see some lines of initialization output in the terminal window confirming that the website is running. Then go to Firefox or Chrome, and go to http://localhost:15434/ to access the site. You will also see any GET or POST requests output to the terminal as well. Skip to **Step 18**

**16.** To run persistently via gunicorn, you must first change the port number at the top of `app.py` to your desired port number within the range 1024 < PORT < 65535. Our application is running on port 15432, so if it is not altered, you will get an error message about the port already being in use.
```python
# Configuration

PORT = 15432  # <== Change to your desired port number
```

**17.** Next, `cd` into the root directory if not already there and run the gunicorn command with your own port number to start web app:
```bash
gunicorn --bind 0.0.0.0:<your-port-number> wsgi:app -D

# Our startup command looks like:
gunicorn --bind 0.0.0.0:15432 wsgi:app -D
```
There will be no confirmation that the app has started but you can confirm that your gunicorn instance is running by entering the following:
```bash
ps ufx | grep gunicorn
```
This should output something like the following:
```bash
lubranoa@flip3  ~/CS340/CS340-Golf-Tracker-DB 
$ps ufx | grep gunicorn
lubranoa  3661  0.0  0.0 218300 16672 ?        S    08:52   0:00 /nfs/stak/users/lubranoa/CS340/CS340-Golf-Tracker-DB/venv/bin/python3 /nfs/stak/users/lubranoa/CS340/CS340-Golf-Tracker-DB/venv/bin/gunicorn --bind 0.0.0.0:15432 wsgi:app -D
lubranoa  3670  0.0  0.0 268264 28788 ?        S    08:52   0:00  \_ /nfs/stak/users/lubranoa/CS340/CS340-Golf-Tracker-DB/venv/bin/python3 /nfs/stak/users/lubranoa/CS340/CS340-Golf-Tracker-DB/venv/bin/gunicorn --bind 0.0.0.0:15432 wsgi:app -D
lubranoa 22537  0.0  0.0 112812   984 pts/5    S+   09:23   0:00      |       \_ grep --color=auto gunicorn
```
Access the gunicorn instance by opening Firefox or Chrome and entering the address http://flipX.engr.oregonstate.edu:XXXX/ changing the X in flipX to your preferred flip server number and the XXXX at the end to your port number. Ours is http://flip3.engr.oregonstate.edu:15432/


**18.** To stop running the web apps, enter either of the following depending on how the web app is running:
   - To kill a localhost webapp, go to the terminal window where the outputs are being output and press `Ctrl+c`
   - To kill all of your gunicorn instances, run:
```bash
pkill -u onid gunicorn
```

## Directory Structure

The files and directories can be in any order but need to be in this specific structure:
```
.
├── .gitignore 
├── README.md
├── app.py
├── wsgi.py
├── requirements.txt
├── venv
├── static
│    └ css               <= Contains all project.css files
│       ├ all-templates.css
│       └ # rest of files
├── database
│    ├ db_connector.py
│    ├ golf-tracker-DDQ.sql
│    └ golf-tracker-DMQ.sql
└── templates               <= Contains all project.j2 files
     ├ main.j2 
     └ # rest of files
```

## Links
- This repo: [CS340-Golf-Tracker-DB](https://github.com/lubranoa/CS340-Golf-Tracker-DB)
- The main starter app linked in our course explorations: [OSU Flask Starter App](https://github.com/osu-cs340-ecampus/flask-starter-app)
- The starter app repo references this repo sometimes: [CS340_starter_app](https://github.com/mlapresta/cs340_starter_app)
- The templating language docs: [Jinja Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/)
