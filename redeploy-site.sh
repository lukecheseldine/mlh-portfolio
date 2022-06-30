#!/bin/bash

tmux kill-server
cd mlh-portfolio
git fetch && git reset origin/main --hard
source venv/bin/activate
pip install -r requirements.txt
pip install pymysql
tmux new-session -d -s portfolio
tmux send -t portfolio source SPACE venv/bin/activate ENTER
tmux send -t portfolio flask SPACE run SPACE --host=0.0.0.0 ENTER
