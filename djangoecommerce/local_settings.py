# coding=utf-8

import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'e_commerce',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': '4n70n10',
}}