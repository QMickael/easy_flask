import os
import sys
import codecs
import shutil
import click
import time

import easy_flask
from .data.utils import colors

#Environment variables
cwd = os.getcwd() #get the current dir
script_dir = os.path.dirname(os.path.realpath(__file__)) #get the data dir (the skeleton)

@click.group()
@click.version_option(version=easy_flask.__version__)
def cli():
    pass


@cli.command()
def start():
    #request the user for appname
    project_name = input('Project name : ') or 'myproject'

    #the path = path/to/the/actually/appname
    fullpath = os.path.join(cwd, project_name)

    #the secret_key for the flask config.py
    secret_key = codecs.encode(os.urandom(32), 'hex').decode('utf-8')

    #the name of skeleton_dir
    skeleton_dir = 'data'
    #template_dir = os.path.join(os.path.join(script_dir, skeleton_dir), os.path.join('project', 'client'))

    # Copying the whole skeleton into the new path. Error if the path already exists
    # TODO error handling here.

    print('Copying the skeleton...\t\t\t\t', end='', flush=True)
    time.sleep(1)
    shutil.copytree(os.path.join(script_dir, skeleton_dir), fullpath)
    print("{green}Ok{end}".format(green=colors.OKGREEN, end=colors.ENDC))


@cli.command()
@cli.option(''
def translate():
