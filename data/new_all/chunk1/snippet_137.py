# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51963760/python-file-is-showing-attributeerror-module-http-has-no-attribute-client
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import http
    _l_(379797)

except ImportError:
    pass
try:
    import requests
    _l_(379799)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(379801)

except ImportError:
    pass
try:
    import urllib3
    _l_(379803)

except ImportError:
    pass
try:
    import pyrebase
    _l_(379805)

except ImportError:
    pass
try:
    import numpy as np
    _l_(379807)

except ImportError:
    pass
try:
    import yagmail
    _l_(379809)

except ImportError:
    pass
try:
    import time
    _l_(379811)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(379813)

except ImportError:
    pass
try:
    import sys
    _l_(379815)

except ImportError:
    pass
try:
    import logging
    _l_(379817)

except ImportError:
    pass
try:
    import colorama
    _l_(379819)

except ImportError:
    pass
try:
    import csv
    _l_(379821)

except ImportError:
    pass
try:
    from random import randint
    _l_(379823)

except ImportError:
    pass
try:
    from numpy import genfromtxt
    _l_(379825)

except ImportError:
    pass
try:
    import sched, time
    _l_(379827)

except ImportError:
    pass
try:
    import threading
    _l_(379829)

except ImportError:
    pass
try:
    import http.client
    _l_(379831)

except ImportError:
    pass
try:
    import firebase_admin
    _l_(379833)

except ImportError:
    pass
try:
    from firebase_admin import credentials
    _l_(379835)

except ImportError:
    pass
try:
    from firebase_admin import db
    _l_(379837)

except ImportError:
    pass


# Fetch the service account key JSON file contents
cred = _c_(379840, _a_(379839, _n_(379838, "credentials", lambda: credentials), "Certificate"), 'service-account-credentials.json')
_l_(379841)
# Initialize the app with a service account, granting admin privileges
_c_(379845, _a_(379843, _n_(379842, "firebase_admin", lambda: firebase_admin), "initialize_app"), _n_(379844, "cred", lambda: cred), {
    'databaseURL': 'https://werrwrrw-catalogue.firebaseio.com'
})
_l_(379846)


config = {
    "apiKey": "BiXzaSdwhjwrhwjjrhwr",
    "authDomain": "whjwrhwjjrhwr.firebaseapp.com",
    "databaseURL": "https://whjwrhwjjrhwr.firebaseio.com",
    "projectId": "whjwrhwjjrhwr",
    "storageBucket": "rewrrrrr.appspot.com",
    "messagingSenderId": "606543434441"
}
_l_(379847)



firebaseuser = _c_(379851, _a_(379849, _n_(379848, "pyrebase", lambda: pyrebase), "initialize_app"), _n_(379850, "config", lambda: config))
_l_(379852)

auth = _c_(379855, _a_(379854, _n_(379853, "firebaseuser", lambda: firebaseuser), "auth"))
_l_(379856)
dbuser = _c_(379859, _a_(379858, _n_(379857, "firebaseuser", lambda: firebaseuser), "database"))
_l_(379860)

subref = _c_(379865, _a_(379864, _c_(379863, _a_(379862, _n_(379861, "db", lambda: db), "reference"), 'Subcribers'), "get"))
_l_(379866)

for key, val in _c_(379869, _a_(379868, _n_(379867, "subref", lambda: subref), "items")):
    _l_(379877)

    subcriber_email = _n_(379870, "val", lambda: val)['Email']
    _l_(379871)
    _c_(379875, _n_(379872, "print", lambda: print), _n_(379873, "key", lambda: key),_n_(379874, "subcriber_email", lambda: subcriber_email))
    _l_(379876)