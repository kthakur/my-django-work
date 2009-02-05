# loc settings for MBP

import os
ROOT_PATH = os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_BACKEND="locmem:///"

DATABASE_NAME = 'djangoport'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.

MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')

MEDIA_URL = 'http://127.0.0.1:8000/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

