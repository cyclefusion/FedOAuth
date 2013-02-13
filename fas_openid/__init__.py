#!/usr/bin/python
#-*- coding: UTF-8 -*-

## These two lines are needed to run on EL6
__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources

# Imports
import flask
from flask.ext.sqlalchemy import SQLAlchemy
from flaskext.babel import Babel

import logging
import logging.handlers

from uuid import uuid4 as uuid

from flask_fas import FAS

# Create the application
APP = flask.Flask(__name__)
# Set up logging (https://fedoraproject.org/wiki/Infrastructure/AppBestPractices#Centralized_logging)
logger = logging.getLogger('openid')
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address='/dev/log', facility=logging.handlers.SysLogHandler.LOG_LOCAL4)
logger.addHandler(handler)
def log_create_message(message):
    if not 'log_id' in flask.session:
        flask.session['log_id'] = uuid().hex
    return '[%(logid)s]%(message)s' % {'logid': session['log_id'], 'message': message}

def log_info(message):
    logger.info(log_create_message(message))

def log_warning(message):
    logger.warning(log_create_message(message))

def log_error(message):
    logger.error(log_create_message(message))

# Set up FASS
FAS = FAS(APP)
APP.config.from_object('fas_openid.default_config')
APP.config.from_envvar('FAS_OPENID_CONFIG', silent=True)
# Set up SQLAlchemy
db = SQLAlchemy(APP)
# Set up Babel
babel = Babel(APP)

# Import the other stuff
import model
import views
