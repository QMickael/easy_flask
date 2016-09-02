import os
import sys
import codecs
import shutil
#import jinja2

from .data.utils import colors

def start():

    #Environment variables
    cwd = os.getcwd() #get the current dir
    script_dir = os.path.dirname(os.path.realpath(__file__)) #get the data dir (the skeleton)
    #request the user for appname
    project_name = input('Project name : ') or 'myproject'

    #the path = path/to/the/actually/appname
    fullpath = os.path.join(cwd, project_name)

    #the secret_key for the flask config.py
    secret_key = codecs.encode(os.urandom(32), 'hex').decode('utf-8')

    #the name of skeleton_dir
    skeleton_dir = 'data'
    template_dir = os.path.join(os.path.join(script_dir, skeleton_dir), os.path.join('project', 'client'))

    # Jinja2 Environment
    #template_loader = jinja2.FileSystemLoader(searchpath=os.path.join(script_dir, "templates"))
    #template_env = jinja2.Environment(loader=template_loader)


    #Create app folder
    print('Creating {0} folder...\t\t\t'.format(project_name), end='', flush=True)
    print("{green}Ok{end}".format(green=colors.OKGREEN, end=colors.ENDC))

    print('Copying the skeleton...\t\t\t', end='', flush=True)
    #copy the data dir (easy_flask/easy_flask/data) into fullpath (actually/app/)
    shutil.copytree(os.path.join(script_dir, skeleton_dir), fullpath)
    print("{green}Ok{end}".format(green=colors.OKGREEN, end=colors.ENDC))

    #Copy the static file and templates
    #print('Copying the templates...\t\t\t', end='', flush=True)
    #shutil.copyfile(os.path.join(script_dir, template_dir), os.path.join(fullpath, 'data/project/client'))


if __name__ == '__main__':
    start()
