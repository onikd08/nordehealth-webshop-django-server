1. Clone the server from github
git clone git@github.com:onikd08/nordehealth-webshop-django-server.git
or
extract zip file name server

2. create and start virtual env
virtualenv env --no-site-packages
source env/bin/activate

3. Install the project dependencies:
pip install -r requirements.txt

4. create a mysql db and add credentials to settings.py
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db-name',
            'USER': 'user-name',
            'PASSWORD': 'user-password',
            'HOST': '127.0.0.1',
            'PORT': 'port-number'
        }
    }


5. Run the following command
python manage.py migrate

6. create admin account
python manage.py createsuperuser

7. After creating superuser run the following commands
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

8. open http://127.0.0.1:8000/api/ on your browser to view the server app.

9. Now go to https://nordhealth-webshop.web.app/ 
you should see the client app running.
