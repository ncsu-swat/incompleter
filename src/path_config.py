import os

PROJECT_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR= os.path.join(PROJECT_DIR, 'data')
LOG_DIR = os.path.join(DATA_DIR, 'logs', 'incompleter')