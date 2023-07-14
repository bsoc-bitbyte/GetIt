import sys
import subprocess
import random


def in_venv():
    return sys.prefix != sys.base_prefix


# Copy content from .env.template to .env
try:

    # Generate a random secret key
    django_secret = ''.join(random.SystemRandom().choice(
        'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))

    with open('.env', 'w') as env:
        env.write('\n')
        env.write('DJANGO_SECRET=' + "'" + django_secret + "'")

    # Check for venv
    if in_venv():
        print('Using Virtualenv')
    else:
        print('Not using Virtualenv')
        exit()

    # Print the python version
    subprocess.run(['python3', '--version'])

    # Install dependencies
    print('Installing dependencies...')
    subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])
    print("Dependencies installed!")

    # Make Migrations
    print('Making migrations...')
    subprocess.run(['python3', 'manage.py', 'makemigrations', 'accounts'])
    subprocess.run(['python3', 'manage.py', 'makemigrations'])
    print("Migrations made!")

    # Migrate the database
    print('Migrating the database...')
    subprocess.run(['python3', 'manage.py', 'migrate'])
    print("Database migrated!")

    # Run the server

    print('Running the server...')
    subprocess.run(['python3', 'manage.py', 'runserver'])

except KeyboardInterrupt:
    print("Process interrupted!")

print("Build Stopped!")
