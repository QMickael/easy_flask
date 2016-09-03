"""
Flask-Skeleton
-------------

Flask with main extensions
	- Admin
	- Login
	- Mail
	- Script
	- and more
"""
from setuptools import setup, find_packages
import easy_flask

setup(
    name='Easy_Flask',
    version='0.1',
    url='http://mickaelonpython.fr/',
    license='BSD',
    author='Mickael Quetelard',
    author_email='mickael.quetelard@gmail.com',
    description='Flask with main extensions',
    long_description=__doc__,
    py_modules=['easy_flask'],
	packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
	install_requires=[
		'alembic',
		'Babel',
		'bcrypt',
		'blinker',
		'cffi',
		'click',
		'coverage',
		'dominate',
		'Flask',
		'Flask-Admin',
		'Flask-BabelEx',
		'Flask-Bcrypt',
		'Flask-Bootstrap',
		'Flask-DebugToolbar',
		'Flask-Login',
		'Flask-Migrate',
		'Flask-Script',
		'Flask-SQLAlchemy',
		'Flask-Testing',
		'Flask-WTF',
		'itsdangerous',
		'Jinja2',
		'Mako',
		'MarkupSafe',
		'pycparser',
		'python-editor',
		'pytz',
		'six',
		'speaklater',
		'SQLAlchemy',
		'visitor',
		'Werkzeug',
		'WTForms',
	],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

	entry_points = {
		'console_scripts': [
			'easy-flask = easy_flask.core:start',
		],
	}
)
