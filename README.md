# django-social-monitor-example

This is a very simple application that makes the collection of tweets according to a fixed term. using django and celery
[](painel.png)  
[](itens.png)
## How to develop?

1. clone repository
2. make a virtualenv with python 3.5.
3. activate virtualenv.
4. Install deps.
5. Configure instance .env
6. run tests.

```console
git clone git@github.com:lffsantos/django-social-monitor-example.git
cd django-social-monitor-example
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## How to run Project?

1- install redis in your machine and run redis-server
2- execute o celery through django
3- run project

```console
cd REDIS_PATH
./redis-server
cd django-social-monitor-example
source .venv/bin/activate
python manage.py runserver
python manage.py celeryd -B -l info
```

This project is an example how to use django with celery... for more explication to access

[http://allissonazevedo.com/2013/06/12/tarefas-assincronas-com-django-e-celery-mutirao-python/](http://allissonazevedo.com/2013/06/12/tarefas-assincronas-com-django-e-celery-mutirao-python/)

realized changes:  
 -> update python2.7 to python3.5  
 -> update django<1.6 to djago 1.9  
  
credits to: 
[https://github.com/allisson/django-social-monitor-example](https://github.com/allisson/django-social-monitor-example)

