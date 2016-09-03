# easy_flask
Create your flask project with main extensions, easily and quickly

## Quick Start

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
