#Source: https://stackoverflow.com/questions/51963760/python-file-is-showing-attributeerror-module-http-has-no-attribute-client
import http
import requests
from bs4 import BeautifulSoup
import urllib3
import pyrebase
import numpy as np
import yagmail
import time
from datetime import datetime, timedelta
import sys
import logging
import colorama
import csv
from random import randint
from numpy import genfromtxt
import sched, time
import threading
import http.client

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Fetch the service account key JSON file contents
cred = credentials.Certificate('service-account-credentials.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://werrwrrw-catalogue.firebaseio.com'
})


config = {
    "apiKey": "BiXzaSdwhjwrhwjjrhwr",
    "authDomain": "whjwrhwjjrhwr.firebaseapp.com",
    "databaseURL": "https://whjwrhwjjrhwr.firebaseio.com",
    "projectId": "whjwrhwjjrhwr",
    "storageBucket": "rewrrrrr.appspot.com",
    "messagingSenderId": "606543434441"
}



firebaseuser = pyrebase.initialize_app(config)

auth = firebaseuser.auth()
dbuser = firebaseuser.database()

subref = db.reference('Subcribers').get()

for key, val in subref.items():
    subcriber_email = val['Email']
    print(key,subcriber_email)