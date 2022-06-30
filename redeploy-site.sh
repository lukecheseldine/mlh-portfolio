#!/bin/bash

git fetch && git reset origin/main --hard
source venv/bin/activate
pip install -r requirements.txt
pip install pymysql
systemctl restart myportfolio
