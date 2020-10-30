# Setup

## RHEL8.2

### To run the flask app

```
dnf install -y git sqlite python38
git clone git@github.com:lshake/fluffy-spoon.git tower_benchmark
cd tower_benchmark/rest
python3.8 -m venv --system-site-packages venv
. ./venv/bin/activate
pip install flask
sqlite3 requests.db < schema.sql
export FLASK_APP=api.py
flask run --host=0.0.0.0
```

### To create the project and resources
Ensure that your private key is stored as ~/.ssh/id_rsa, or set the playbook variable "tower_ssh_

```
cd tower_benchmark/ansible
export TOWER_PASSWORD=xxxxx
export TOWER_USERNAME=admin
export TOWER_HOST=tower.example.com
ansible-playbook ./project.yml -i "[localhost,]"
```

### To run the load injector
```
cd tower_benchmark/ansible
python3.8 -m venv --system-site-packages venv
. ./venv/bin/activate
pip install ansible
ansible-galaxy collection install awx.awx
export TOWER_PASSWORD=xxxxx
export TOWER_USERNAME=admin
export TOWER_HOST=tower.example.com
ansible-playbook ./run.yml -i "[localhost,]"
```



