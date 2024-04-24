#wsgi.py
import os, sys
# Calculate the path based on the location of the WSGI script.
#apache_configuration= os.path.dirname(__file__)
#project = os.path.dirname(apache_configuration)
#workspace = os.path.dirname(project)
#sys.path.append(workspace)
#sys.path.append(project)

# Add the path to 3rd party django application and to django itself.
sys.path.append('/home/sac/GetIt/backend')
sys.path.append('/home/sac/GetIt/backend/venv/lib/python3.8/site-packages/')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'ozone.settings'

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# import os

# Environment Variables
os.environ["STRIPE_SECRET_KEY"]="sk_test_51OK0jxSCqTflNj8Zy1p4XuUEKULp8shZYFeBAh2V1mvRs6YiVEs7WqWEHrJItLaMLj1ppZfkbg8mrtPvhbCW7Znv00yKkwgWDj"
os.environ["DJANGO_SECRET"]="3eam5ip0cmij@xce!b*#(evcr=0(v2m11k@)^nx4!*^2s1k1-g"
os.environ["STRIPE_WEBHOOK_SECRET"]="whsec_a965db034f97cfff1fcfde9f8e216acbeb0e189ced37f3592896659f8753f225"
os.environ["DJANGO_SETTINGS_MODULE"]="core.settings.production"
os.environ["ALLOWED_HOSTS"]="['127.0.0.1', '172.27.16.191', '14.139.241.217', '58.84.25.100', '103.59.142.75', 'https://www.iiitdmj.ac.in/sac.iiitdmj.ac.in/', 'sac.iiitdmj.ac.in', 'getit-server.iiitdmj.ac.in']"
os.environ["UPI_API_KEY"]="49bdf822-962c-44eb-a41f-a8605f233656"
os.environ["DEBUG"]="False"

import logging
logging.basicConfig(stream=sys.stderr)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
