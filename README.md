## Installation

### donwload source code
git clone https://github.com/luckyfanghe/django-api.git

### install virtual environment
python3 -m venv env <br/>
source env/bin/activate  # On Windows use `env\Scripts\activate`

### install packages
pip install --upgrade pip <br/>
pip install -r requirements.txt

### setup database
python manage.py migrate

### start the web server in local:
python manage.py runserver

### start the web server in cloud:
sudo python manage.py runserver 0.0.0.0:8000

#### add ip address or domain into ALLOWED_HOSTS in settings.py
es: ALLOWED_HOSTS = ['userlocation.org', '123.123.123.123']

## admin approval/decline page
http://localhost:8000/pendinglocations
