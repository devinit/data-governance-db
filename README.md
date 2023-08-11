# Data Governance DB

## Template setup

1. Replace string "Data Governance DB" with the name of your project
2. Replace string "data-governance-db" with the name of your project repository slug
3. Replace string "datagov.devinit.org" with domain of your project

## Setup
```
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl python3-pip

sudo adduser website
sudo usermod -a -G www-data website

su website
cd ~
git clone https://github.com/devinit/data-governance-db.git

cd data-governance-db

cp .env-example .env

pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser

exit
chown -R website:www-data /home/website
cd /home/website/data-governance-db

sudo cp config/gunicorn/gunicorn.socket /etc/systemd/system/gunicorn.socket
sudo cp config/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service

sudo systemctl daemon-reload

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo cp config/nginx/datagov.devinit.org /etc/nginx/sites-available/datagov.devinit.org
sudo ln -s /etc/nginx/sites-available/datagov.devinit.org /etc/nginx/sites-enabled
sudo systemctl restart nginx

sudo ufw allow 'Nginx Full'

sudo snap install core; sudo snap refresh core
sudo apt remove certbot
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

sudo certbot --nginx -d datagov.devinit.org

sudo systemctl status snap.certbot.renew.service
sudo certbot renew --dry-run
```

## Deployment
```
su website
cd ~/data-governance-db
git pull origin main
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py initial_import
exit
sudo systemctl restart gunicorn
```