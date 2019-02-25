#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals, absolute_import

def calc_eval(unsanitized):
    if isinstance(unsanitized, str):
        sanitized = ''.join(c for c in unsanitized if c in '0123456789*/+-')
        return eval(sanitized)
    else:
        return unsanitized


######## NOT SETTINGS, JUST BOILER PLATE ##############
import json, os

VERSION = '0.5'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LIBS_DIR = os.path.join(os.path.dirname(ROOT_DIR), 'libs')

######## END OF BOILER PLATE ##############

# debug will get you error message and auto reload
# don't set this to True in production
DEBUG = json.loads(os.getenv('DEBUG', 'false'))

# Should the application serve static files on it's own ?
# IF yes, set the absolute path to the static files.
# If no, set it to None
# In dev this is handy, in prod you probably want the HTTP servers
# to serve it, but it's OK for small traffic to set it to True in prod too.
STATIC_FILES_ROOT = os.path.join(ROOT_DIR, 'static')

# If True, will link the compressed verion of the js and css files,
# otherwise, will use the ordinary files
COMPRESSED_STATIC_FILES = json.loads(os.getenv('COMPRESSED_STATIC_FILES', 'true'))

# absolute path where the paste files should be store
# default in projectdirectory/static/content/
# use "/" even under Windows
PASTE_FILES_ROOT = os.getenv('PASTE_FILES_ROOT', '/data')

# a tuple of absolute paths of directory where to look the template for
# the first one will be the first to be looked into
# if you want to override a template, create a new dir, write the
# template with the same name as the one you want to override in it
# then add the dir path at the top of this tuple
TEMPLATE_DIRS = (
    '/views',
    '/app/zerobin/views'
)
if os.getenv('CUSTOM_TEPLATE_DIR') is not None:
    TEMPLATE_DIRS = [os.getenv('CUSTOM_TEMPLATE_DIR')] + TEMPLATE_DIRS

# Port and host the embeded python server should be using
# You can also specify them using the --host and --port script options
# which have priority on these settings
HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', '80')

# User and group the server should run as. Set to None if it should be the
# current user. Some OS don't support it and if so, it will be ignored.
USER = os.getenv('USER', 'null')
GROUP = os.getenv('GROUP', 'null')

# Display a tiny counter for pastes created.
# Be carreful if your site have to many pastes this can hurt your hard drive performances.
# Refresh counter interval. Default to every minute after a paste.
DISPLAY_COUNTER = json.loads(os.getenv('DISPLAY_COUNTER', 'true'))
REFRESH_COUNTER = calc_eval(os.getenv('REFRESH_COUNTER', 60 * 1))

# Names/links to insert in the menu bar.
# Any link with "mailto:" will be escaped to prevent spam
MENU = json.loads(os.getenv('MENU', '[["Home","/"],["Download 0bin","https://github.com/sametmax/0bin"],["Faq","/faq/"],["Contact","mailto:your@email.com"]]'))

# limit size of pasted text in bytes. Be careful allowing too much size can
# slow down user's browser
MAX_SIZE = calc_eval(os.getenv('MAX_SIZE', 1024 * 500))

# length of base64-like paste-id string in the url, int from 4 to 27 (length of sha1 digest)
# total number of unique pastes can be calculated as 2^(6*PASTE_ID_LENGTH)
# for PASTE_ID_LENGTH=8, for example, it's 2^(6*8) = 281 474 976 710 656
PASTE_ID_LENGTH = calc_eval(os.getenv('PASTE_ID_LENGTH', 8))

# if burn_after_reading is selected
# if this pageload is seconds after the creation date,
# we don't delete the paste because it means it's the redirection
# to the paste that happens during the paste creation
# this configures the number of seconds to wait.
BURN_ACTIVATION_SECONDS = calc_eval(os.getenv('BURN_ACTIVATION_SECONDS', 10))
