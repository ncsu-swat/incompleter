#Source: https://stackoverflow.com/questions/72495771/attributeerror-module-wsgi-has-no-attribute-application
import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'app.py')
application = wsgi.application