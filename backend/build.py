import sys
import subprocess
import random


def in_venv():
    return sys.prefix != sys.base_prefix


# Copy content from .env.template to .env
try:
    # Check for venv
    if in_venv():
        print('Using Virtualenv')
    else:
        print('Not using Virtualenv')
        exit()

    # Print the python version
    subprocess.run(['python', '--version'])

    # Install dependencies
    print('Installing dependencies...')
    subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])
    print("Dependencies installed!")

    # Make Migrations
    print('Making migrations...')
    subprocess.run(['python', 'manage.py', 'makemigrations', 'accounts'])
    subprocess.run(['python', 'manage.py', 'makemigrations', 'products'])
    subprocess.run(['python', 'manage.py', 'makemigrations', 'events'])
    subprocess.run(['python', 'manage.py', 'makemigrations', 'tickets'])
    subprocess.run(['python', 'manage.py', 'makemigrations', 'orders'])
    subprocess.run(['python', 'manage.py', 'makemigrations'])
    print("Migrations made!")

    # Migrate the database
    print('Migrating the database...')
    subprocess.run(['python', 'manage.py', 'migrate'])
    print("Database migrated!")

    # Run the server

    print('Running the server...')
    subprocess.run(['python', 'manage.py', 'runserver'])

except KeyboardInterrupt:
    print("Process interrupted!")

print("Build Stopped!")
