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

getting all boys names list 

GET (with simple pagination)
```
http://127.0.0.1:8000/api/v1/test/?page=1
```

Method for search boys names
POST
```
http://127.0.0.1:8000/api/v1/test/


 param request -> JSON string
 search_phrase: str,
 age_distribution: list
 search_criteria: str (begin, end, middle) default: all
 frequency: list (based on NamesModel frequency field)
 limit: int
 skip: int
```