# Python and virtualenv installation an ubuntu or debian OS
```sh
> sudo apt update
> sudo apt install python3-pip python3-dev libpq-dev
> sudo pip3 install virtualenv
```
> Python version 3.6+

# Git installation and configuration 
```sh
> sudo apt install git
> git config --global user.name "your username"
> git config --global user.email "your email"
```

# Create virtualenv

```sh
> mkdir $DIRNAME/workspace # for example $DIRNAME = /home/site/medcretech
> cd $DIRNAME/workspace
> virtualenv venv
```

## requirement python installation and create src workspace

```sh
> cd $DIRNAME/workspace/venv
> source bin/activate
> mkdir test-mdsoft && cd test-mdsoft
> git clone https://github.com/bnsMedFaouzi/test-mdsoft.git
> git checkout BrancheName # for example BrancheName = master or dev
> pip install -r requirements.txt
```

## Run exercises
### Ex1
```sh
> python exercice_1.py
```
### Ex2
```sh
> cd exercice_2
> python xlsx_to_json.py
```
### Ex3
```sh
> python -m unittest test_xlsx_to_list.py 
```