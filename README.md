# easy_flask
Create your flask project with main extensions, easily and quickly.
This tools use my fork [flask-skeleton](https://github.com/QMickael/flask-skeleton.git) from realpython flask-skeleton [repo](https://github.com/realpython/flask-skeleton.git). Before use easy_flask, be sure you know [Blueprints](http://flask.pocoo.org/docs/0.11/blueprints/) development !


### Next features
- Add translation function with cli
- Add Flask-Mail

### Installation

0. Create a project folder
1. Activate a virtualenv
2. Install package with pip (not actually on pypi repo libraries):

```sh
$ pip install git+https://github.com/QMickael/easy_flask.git
```

### Basics

Starting a project:
```sh
$ easy-flask start
```

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)

If you get an admin page got to the adress [http://localhost:5000/admin](http://localhost:5000/admin)

> Want to specify a different port?

> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
