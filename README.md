# CS340-Golf-Tracker-DB
## How to set up application
1. SSH to your flipX server of choice
2. cd into the directory you want the repo in
3. If you have github ssh set up like they showed us in this course and you want to clone using ssh, run the first line. Otherwise, if you want to use username/password, run the second line.

```
git clone git@github.com:lubranoa/CS340-Golf-Tracker-DB.git

# OR

git clone https://github.com/lubranoa/CS340-Golf-Tracker-DB.git
```

4. cd into the repo and set up python virtual environments:
```
pip3 install --user virtualenv
python3 -m venv ./venv
```
5. Activate virtual environment (always do this when working on the project)
```
source ./venv/bin/activate
```
   - If you want to confirm the virtual environment is active, run the following commad:
```
which python3
# should return <path_to_your_repo_folder>/venv/bin/python3
```
   - To leave the virtual environment just run ```deactivate```
6. Install dependencies in ```requirements.txt```
