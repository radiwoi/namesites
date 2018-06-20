**RUNNING PROJECT LOCALLY**

In current folder make these commands:

1) Create virtual environment if not exists:
```
	virtualenv -p python3 venv
```
2) Activate virtual environment 
```
	source venv/bin/activate
```
3) ***IMPORTANT***: install next libraries before the installing requirements to avoid mysql errors:  
```
	sudo apt-get install python-dev python3-dev 
	sudo apt-get install libmysqlclient-dev
	sudo apt-get install python3-mysqldb 
```
4) Set up all required packages  from `requirements.txt` file:
```
	pip install -r requirements.txt
```
5) Run database migrations  
```
	python manage.py migrate
```

6) Finally, start the project:  
```
	python manage.py runserver
```

7) actual routes

getting all boys names list (with simple pagination)
```
Method: GET
http://127.0.0.1:8000/api/v1/test/?page=1

Returns json response
```

Method for search boys names

```
http://127.0.0.1:8000/api/v1/test/
method: POST

 param: request -> JSON string
 search_phrase: str,
 age_distribution: list
 search_criteria: str (begin, end, middle)
 frequency: list (based on NamesModel frequency field)
 letters_range: str
 double_name: bool
 limit: int
 skip: int
 
 Returns json response
```

PS: setup email sender using Celery

```
$ sudo rabbitmqctl add_user myuser mypassword
$ sudo rabbitmqctl add_vhost myvhost
$ sudo rabbitmqctl set_user_tags myuser mytag
$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

To start the server:

$ sudo rabbitmq-server
you can also run it in the background by adding the -detached option (note: only one dash):

$ sudo rabbitmq-server -detached
Never use kill (kill(1)) to stop the RabbitMQ server, but rather use the rabbitmqctl command:

$ sudo rabbitmqctl stop



CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672/'

# SetUp Celery Email backend, and the SMTP server configurations

EMAIL_HOST = 'SMTP_HOST'

EMAIL_PORT = 'SMTP_PORT'

EMAIL_HOST_USER = 'SMTP_USER'

EMAIL_HOST_PASSWORD = 'SMTP_PASSWORD'

EMAIL_USE_TLS = True   # TLS settings

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

EMAIL_HEADER = 'Trololo'



Running Celery
$ celery -A my_app worker -l info and keep the terminal session opened.
```