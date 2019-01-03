#!usr/bin/env bash

#indicate where 
apt-get -y update

#install dependencies
apt-get -y install postgresql postgresql-contrib python3-pip screenfetch virtualenv

#create virtual env
virtualenv -p python3 --no-site-packages run/lib

#activate virtual env
source run/lib/bin/activate

#pip3
pip3 install flask psycopg2

pip3 freeze > /run/setup/requirements.txt

#install dependencies
pip3 install -r setup/requirements.txt
