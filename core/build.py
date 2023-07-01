import os
import sys
import subprocess
import random

def in_venv():
    return sys.prefix != sys.base_prefix

# Copy content from .env.template to .env
try :
    with open ('.env.template', 'r') as template, open ('.env', 'w') as env:
        env.write (template.read ())

    # Generate a random secret key
    django_secret = ''.join (random.SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range (50))

    with open('.env', 'a') as env :
        env.write ('\n')
        env.write ('DJANGO_SECRET=' + django_secret)

    # Create and activate virtual environment
    subprocess.run (['python3', '-m', 'venv', '.venv'])

    if in_venv():
        print('Using Virtualenv')
    else:
        print('Not using Virtualenv')
        exit()

    # Print the python version
    subprocess.run (['python3', '--version'])

    # Install dependencies
    print('Installing dependencies...')
    subprocess.run (['pip3', 'install', '-r', 'requirements.txt'])
    print("Dependencies installed!")

    # Make Migrations
    print('Making migrations...')
    subprocess.run (['python3', 'manage.py', 'makemigrations'])
    print("Migrations made!")

    # Migrate the database
    print('Migrating the database...')
    subprocess.run (['python3', 'manage.py', 'migrate'])
    print("Database migrated!")

    # Run the server

    print('Running the server...')
    subprocess.run (['python3', 'manage.py', 'runserver'])

except KeyboardInterrupt :
    print("Process interrupted!")
    
print("Build Stopped!")

