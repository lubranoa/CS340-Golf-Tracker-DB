# CS340-Golf-Tracker-DB

Created by Conner Marchell and Alex Lubrano
CS 340 - Introduction to Databases Portfolio Project

## Project Description
Description goes here.

## Links
- Our repo: [CS340-Golf-Tracker-DB](https://github.com/lubranoa/CS340-Golf-Tracker-DB)
- The main starter app linked in our course explorations: [OSU Flask Starter App](https://github.com/osu-cs340-ecampus/flask-starter-app)
- The starter app repo references this repo sometimes: [CS340_starter_app](https://github.com/mlapresta/cs340_starter_app)
- The templating language docs: [Jinja Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/)

## How to set up application
**1.** SSH to your flipX server of choice

**2.** cd into the directory you want the repo in

**3.** If you have github ssh set up like they showed us in this course and you want to clone using ssh, run the first line. Otherwise, if you want to use username/password, run the second line.

```
git clone git@github.com:lubranoa/CS340-Golf-Tracker-DB.git

# OR

git clone https://github.com/lubranoa/CS340-Golf-Tracker-DB.git
```

**4.** cd into the repo and set up python virtual environments:
```
pip3 install --user virtualenv
python3 -m venv ./venv
```

**5.** Activate virtual environment (always do this when working on the project)
```
source ./venv/bin/activate
```
   - If you want to confirm the virtual environment is active, run the following commad:
```
which python3
# should return <path_to_your_repo_folder>/venv/bin/python3
```
   - To leave the virtual environment just run ```deactivate```

**6.** Install dependencies in ```requirements.txt``` by running:
```
pip3 install -r requirements.txt
```

**7.** Create .env file in root directory and add the following lines to it, changing the bottom three values to your own stuff. Ensure that the .env file is in the .gitignore file.
```
340DBHOST = 'classmysql.engr.oregonstate.edu'
340DBUSER = '<your_osu_db_user_name>'  # cs340_onid
340DBPW = '<your_osu_db_password>'     # 4-digit pw to log into db
340DB = '<your_osu_db_name>'           # cs340_onid
```

**8.** (Optional) cd into the database directory and create a backup of your current database:
```
mysqldump -u cs340_onid -h classmysql.engr.oregonstate.edu -p cs340_onid > backup.sql
```

**9.** If not already in database directory, cd into it, then log in to your database, by running:
```
mysql -u cs340_onid -h classmysql.engr.oregonstate.edu -p cs340_onid
```

**10.** (Optional?) Drop old tables from your osu database using ```DROP TABLES your_table1, your_table2;```

**11.** Load ```golf_tracker_DDL.sql``` into your database, entering:
```
source golf_tracker_DDL.sql
```

**12.** Run the app using Gunicorn:
```
gunicorn -b 0.0.0.0:15432 -D app:app
```
        
   - To kill all your instances of Gunicorn, run:
```
pkill -u onid gunicorn
```

   - For more information check the [bottom](https://github.com/osu-cs340-ecampus/flask-starter-app#deploying-the-migrated-project-on-osus-flip-server) of the 340 Flask Starter App repo

**13.** Navigate to web app address at (http://flipX.engr.oregonstate.edu:15432/) changing the X to your preferred flip server.

At this point, it should work!