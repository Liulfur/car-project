import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'cars.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CRSF_ENABLED = True
SECRET_KEY = 'A.K}_OU-lMi603;'

DATABASE_PATH = os.path.join(basedir, DATABASE)