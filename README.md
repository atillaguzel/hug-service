# hug-service
Hug service boilerplate


Command line interaction:
```
python app.py Atilla 39
```


Using uwsgi:
```
uwsgi --http 0.0.0.0:8000 --wsgi-file app.py --callable __hug_wsgi__
```


Or, using gunicorn:
```
gunicorn app:__hug_wsgi__
```