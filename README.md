# Django project template

## Template setup

1. Replace string "Django Project Template" with the name of your project
2. Replace string "django-project-template" with the name of your project repository slug
3. Replace string "website.devinit.org" with domain of your project

## Setup
```
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl python3-pip

sudo adduser website
sudo usermod -a -G www-data website

su website
cd ~
git clone https://github.com/devinit/django-project-template.git

cd django-project-template

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
cd /home/website/django-project-template

sudo cp config/gunicorn/gunicorn.socket /etc/systemd/system/gunicorn.socket
sudo cp config/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service

sudo systemctl daemon-reload

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo cp config/nginx/website.devinit.org /etc/nginx/sites-available/website.devinit.org
sudo ln -s /etc/nginx/sites-available/website.devinit.org /etc/nginx/sites-enabled
sudo systemctl restart nginx

sudo ufw allow 'Nginx Full'

sudo snap install core; sudo snap refresh core
sudo apt remove certbot
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

sudo certbot --nginx -d website.devinit.org

sudo systemctl status snap.certbot.renew.service
sudo certbot renew --dry-run
```

## Deployment
```
su website
cd ~/django-project-template
git pull origin main
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py initial_import
exit
sudo systemctl restart gunicorn
```